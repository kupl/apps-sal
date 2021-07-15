import sys
sys.setrecursionlimit(10**7)

def dfs(v, visited, counter):
    visited[v] = 1
    for nv in G[v]:
        if visited[nv]:
            continue
        visited[nv] = 1
        counter.append(1)
        dfs(nv, visited, counter)
    return

n, m = map(int, input().split())
G = [[] for _ in range(n)]
visited = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

max_friends = 0
for i in range(n):
    if visited[i]:
        continue
    friends = []
    dfs(i, visited, friends)
    max_friends  = max(max_friends, sum(friends) + 1)

print(max_friends)
