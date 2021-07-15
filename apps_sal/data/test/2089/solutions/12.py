from collections import deque


def bfs(v):
    dist = [-1] * n
    used = [0] * n
    q = deque([])
    q.append(v)
    dist[v] = 0
    used[v] = 1
    while q:
        x = q.popleft()
        for i in range(len(graph[x])):
            if not used[graph[x][i]]:
                used[graph[x][i]] = 1
                dist[graph[x][i]] = dist[x] + 1
                q.append(graph[x][i])
    return dist
  
        
n, m, s, t = map(int, input().split())
s -= 1
t -= 1
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
dt = bfs(t)
ds = bfs(s)
dist = ds[t]
ans = 0
for u in range(n - 1):
    for v in range(u + 1, n):
        if ds[u] + dt[v] + 1 >= dist and ds[v] + dt[u] + 1 >= dist:
            ans += 1
print(ans - m)
