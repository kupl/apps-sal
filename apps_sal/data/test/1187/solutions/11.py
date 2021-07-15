import sys
import collections
import functools

n,m  = list(map(int, input().strip().split()))
graph = collections.defaultdict(list)
edges = []
for i in range(m):
    u,v = list(map(int, input().strip().split()))
    graph[u].append([v,i])
    edges.append((u,v))

ans = [1]*m
visited = [False for _ in range(5000)]
seen = [False for _ in range(5000)]

def dfs(u):
    seen[u] = visited[u] = True
    for v, i in graph[u]:
        if seen[v]:
            ans[i] = 2
        elif not visited[v]:
            ans[i] = 1
            dfs(v)
    seen[u] = False

for u, v in edges:
    if visited[u]: continue
    dfs(u)

print(max(ans))
print(' '.join(str(i) for i in ans))

