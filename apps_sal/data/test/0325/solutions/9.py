from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
from scipy.sparse import csr_matrix
from collections import defaultdict

n, m, p = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(m)]
INF = 10 ** 9

fwd = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]

for a, b, c in abc:
    fwd[a].append(b)
    rev[b].append(a)


def dfs(s, adj):
    stack = [s]
    arrived = [False] * (n + 1)
    arrived[s] = True
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not arrived[v]:
                arrived[v] = True
                stack.append(v)

    return arrived


can_go_fwd = dfs(1, fwd)
can_go_rev = dfs(n, rev)

data = defaultdict(lambda: INF)
for a, b, c in abc:
    if can_go_fwd[a] and can_go_rev[b]:
        data[(a, b)] = min(data[(a, b)], p - c)

row = []
col = []
cost = []
for (a, b), c in list(data.items()):
    row.append(a)
    col.append(b)
    cost.append(c)

g = csr_matrix((cost, (row, col)), shape=(n + 1, n + 1))

try:
    dist = bellman_ford(g, indices=[1]).astype(int)
    ans = max(0, -dist[0][n])
    print(ans)
except NegativeCycleError:
    print((-1))

