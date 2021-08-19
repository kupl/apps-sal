from collections import deque
import sys
(n, m) = map(int, input().split())
graph = [[] for _ in range(3 * n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    graph[a].append(b + n)
    graph[a + n].append(b + 2 * n)
    graph[a + 2 * n].append(b)
dist = [-3] * (3 * n + 1)
dist[0] = 0
(s, t) = map(int, input().split())
dist[s] = 0
d = deque()
d.append(s)
while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -3:
            continue
        dist[i] = dist[v] + 1
        d.append(i)
print(dist[t] // 3)
