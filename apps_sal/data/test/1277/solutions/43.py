import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
(n, u, v) = map(int, input().split())
graph = defaultdict(list)
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(u):
    dist = [-1] * (n + 1)
    stack = [u]
    dist[u] = 0
    while stack:
        u = stack.pop()
        nxt = dist[u] + 1
        for v in graph[u]:
            if dist[v] >= 0:
                continue
            dist[v] = nxt
            stack.append(v)
    return dist


dist_u = dfs(u)
dist_v = dfs(v)
ans = 0
for (x, y) in zip(dist_u, dist_v):
    if x < y:
        ans = max(ans, y - 1)
print(ans)
