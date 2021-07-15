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
visited = set()

def dfs(u, seen):
    seen.add(u)
    visited.add(u)
    for v, i in graph[u]:
        if v in seen:
            ans[i] = 2
        elif v not in visited:
            ans[i] = 1
            dfs(v, seen)
    seen.remove(u)

seen = set()

for u, v in edges:
    if u in visited: continue
    dfs(u, seen)

print(max(ans))
print(' '.join(str(i) for i in ans))

