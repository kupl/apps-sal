from collections import deque
N = int(input())
dist = {}
graph = [[] for i in range(N)]
for i in range(1, N):
    (u, v, w) = list(map(int, input().split()))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
    dist[u - 1, v - 1] = w
q = deque()
q.append(0)
color = [-1] * N
color[0] = 0
while q:
    now = q.popleft()
    for adj in graph[now]:
        if color[adj] == -1:
            if now < adj:
                color[adj] = color[now] + dist[now, adj]
            else:
                color[adj] = color[now] + dist[adj, now]
            q.append(adj)
for i in range(N):
    print(color[i] % 2)
