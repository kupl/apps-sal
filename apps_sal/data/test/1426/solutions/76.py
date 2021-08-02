from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(3 * N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[3 * u].append(3 * v + 1)
    graph[3 * u + 1].append(3 * v + 2)
    graph[3 * u + 2].append(3 * v)

S, T = map(int, input().split())
S -= 1
T -= 1
dist = [-1] * (3 * N)
dist[3 * S] = 0
d = deque([3 * S])
while d:
    node = d.popleft()
    children = graph[node]
    for child in children:
        if dist[child] < 0:
            dist[child] = dist[node] + 1
            d.append(child)

if dist[3 * T] > 0:
    print(dist[3 * T] // 3)
else:
    print(-1)
