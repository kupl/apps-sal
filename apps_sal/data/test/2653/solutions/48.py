import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

d = defaultdict(int)
for _ in range(Q):
    p, x = map(int, input().split())
    d[p - 1] += x
visited = [False] * N
cnt = [0] * N


def dfs(n, acc):
    cnt[n] = acc
    for m in edges[n]:
        if not visited[m]:
            visited[m] = True
            dfs(m, acc + d[m])


visited[0] = True
dfs(0, d[0])
print(*cnt)
