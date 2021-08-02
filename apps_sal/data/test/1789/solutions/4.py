import heapq
a, b, x, y = list(map(int, input().split()))
dist = [10**30 for i in range(200)]
G = [[] for i in range(200)]
a -= 1; b -= 1; b += 100
for i in range(99):
    G[i].append((i + 1, y))
    G[i + 1].append((i, y))
    G[i + 100].append((i + 1 + 100, y))
    G[i + 1 + 100].append((i + 100, y))
for i in range(100):
    G[i].append((i + 100, x))
    G[i + 100].append((i, x))
for i in range(99):
    G[i + 1].append((i + 100, x))
    G[i + 100].append((i + 1, x))
dist[a] = 0
q = []
heapq.heappush(q, (0, a))
while(q):
    d, r = heapq.heappop(q)
    if dist[r] < d:
        continue
    for p, cost in G[r]:
        if dist[p] > dist[r] + cost:
            dist[p] = dist[r] + cost
            heapq.heappush(q, (dist[p], p))
print((dist[b]))
