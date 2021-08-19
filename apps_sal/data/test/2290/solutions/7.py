import sys
from collections import defaultdict


def dfs(s, compN):
    visited[s] = compN
    queue = set(adj[s])
    maxV = s
    while queue:
        v = queue.pop()
        if not visited[v]:
            visited[v] = compN
            maxV = max(maxV, v)
            queue.update(adj[v])
    return maxV


def countEdges(adj, n, m):
    compN = 0
    comps = []
    for s in range(1, n + 1):
        if not visited[s]:
            compN += 1
            minV = s
            maxV = dfs(s, compN)
            comps.append((minV, compN, 0))
            comps.append((maxV, compN, 1))

    comps.sort()
#     print(comps)
    opened = set()
    ctr = 0
    for v, compN, closed in comps:
        if closed:
            opened.remove(compN)
        else:
            if opened:
                ctr += 1
            opened.add(compN)
    return ctr


# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, s.split())) for s in sys.stdin)

n, m = next(reader)
adj = defaultdict(list)
for _ in range(m):
    i, j = next(reader)
    adj[i].append(j)
    adj[j].append(i)
visited = [False] * (n + 1)
ans = countEdges(adj, n, m)
print(ans)

# inf.close()
