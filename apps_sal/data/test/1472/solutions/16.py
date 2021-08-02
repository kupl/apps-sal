from collections import deque
from collections import Counter

n, x, y = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(1, n):
    a, b = i, i + 1
    graph[a].append(b)
    graph[b].append(a)
graph[x].append(y)
graph[y].append(x)

l = []
for j in range(1, n + 1):
    dist = [-1] * (n + 1)
    dist[0] = 0
    dist[j] = 0

    d = deque()
    d.append(j)

    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    l.extend(dist[1:])

c = Counter(l)
for i in range(1, n):
    print(int(c[i] / 2))
