from sys import stdin
from heapq import heappop, heappush

n, m = [int(x) for x in stdin.readline().split()]

graph = [{} for x in range(n + 1)]

for e in range(m):
    u, v, w = [int(x) for x in stdin.readline().split()]
    graph[u][v] = (w, e)
    graph[v][u] = (w, e)

u = int(stdin.readline())

visited = set()
dist = [(float('inf'), 0) for x in range(n + 1)]
pathTo = [0 for x in range(n + 1)]
dist[u] = (0, 0)
q = []
heappush(q, (0, u))

while q:
    d, v = heappop(q)
    if not v in visited:
        visited.add(v)
        for e in graph[v]:
            if (d + graph[v][e][0], graph[v][e][0]) < dist[e]:
                dist[e] = (d + graph[v][e][0], graph[v][e][0])
                pathTo[e] = graph[v][e][1]
                heappush(q, (d + graph[v][e][0], e))

total = 0

for x in dist[1:]:
    total += x[1]

print(total)
for x in range(1, n + 1):
    if x != u:
        print(pathTo[x] + 1, end=' ')
