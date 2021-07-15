n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))

init_v = 0
INF = float('inf')
dist = [INF]*n
dist[init_v] = 0
negative_cycle = 0
for i in range(2*n):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        dist[v2] = dist[v]+c
        if i >= n-1 and v2 == n-1:
            negative_cycle = 1

if negative_cycle:
    print('inf')
else:
    print(-dist[-1])
