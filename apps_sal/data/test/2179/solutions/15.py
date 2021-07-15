import heapq

n, m = list(map(int, input().split()))
ed = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(m)]
src = int(input())

g = [[] for _ in range(n + 1)]
for i, (u, v, w) in enumerate(ed):
    g[u].append((i, v, w))
    g[v].append((i, u, w))

pq = [(0, 0, src)]
dist = [(10 ** 15, 0)] * (n + 1)
up = [0] * (n + 1)
while pq:
    d, e, u = heapq.heappop(pq)
    if (d, e) > dist[u]:
        continue
    for i, v, w in g[u]:
        if (d + w, w) < dist[v]:
            dist[v] = d + w, w
            up[v] = i
            heapq.heappush(pq, (d + w, w, v))

t = [up[u] for u in range(1, n + 1) if u != src]
print(sum(ed[e][2] for e in t))
print(*t)

