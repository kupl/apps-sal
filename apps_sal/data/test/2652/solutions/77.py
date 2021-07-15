import sys
import heapq
input = sys.stdin.readline


n = int(input())
Xs = []
Ys = []
for i in range(n):
    x, y = map(int, input().split())
    Xs.append((x-1, i))
    Ys.append((y-1, i))

Xs.sort()
Ys.sort()

edges = [[] for _ in range(n)]
for i in range(n-1):
    x, node = Xs[i]
    nx, new_node = Xs[i+1]
    edges[node].append((nx-x, new_node))
    edges[new_node].append((nx-x, node))

for i in range(n-1):
    y, node = Ys[i]
    ny, new_node = Ys[i+1]
    edges[node].append((ny-y, new_node))
    edges[new_node].append((ny-y, node))

seen = [False] * n
dist = [float('INF')] * n
todo = [(0, 0)]

while todo:
    d, node = heapq.heappop(todo)
    if seen[node]:
        continue
    seen[node] = True
    dist[node] = d

    for edge in edges[node]:
        nd, to = edge
        if dist[to] <= nd:
            continue
        heapq.heappush(todo, (nd, to))

print(sum(dist))
