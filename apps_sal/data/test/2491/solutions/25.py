(n, m) = map(int, input().split())
edges = []
for _ in range(m):
    (a, b, c) = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))
init_v = 0
INF = float('inf')
dist = [INF] * n
dist[init_v] = 0
for i in range(n):
    for (v, v2, c) in edges:
        if dist[v2] <= dist[v] + c:
            continue
        dist[v2] = dist[v] + c
negative = [0] * n
for i in range(n):
    for (v, v2, c) in edges:
        if dist[v2] <= dist[v] + c:
            continue
        dist[v2] = dist[v] + c
        negative[v2] = 1
if negative[-1]:
    print('inf')
else:
    print(-dist[-1])
