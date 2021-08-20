import heapq
from itertools import permutations
(n, m, r) = list(map(int, input().split()))
R = list([int(x) - 1 for x in input().split()])
edges = [[] for _ in range(n)]
for _ in range(m):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges[a].append((c, b))
    edges[b].append((c, a))


def dijkstra(init_v):
    next_v = [(0, init_v)]
    INF = 10 ** 18
    dist = [INF] * n
    dist[init_v] = 0
    while next_v:
        (d, v) = heapq.heappop(next_v)
        if dist[v] < d:
            continue
        for (d, v2) in edges[v]:
            if dist[v2] <= dist[v] + d:
                continue
            dist[v2] = dist[v] + d
            heapq.heappush(next_v, (dist[v2], v2))
    return dist


dists = []
for x in R:
    dist = dijkstra(x)
    dists.append(dist)
INF = 10 ** 18
ans = INF
for subset in permutations(list(range(r))):
    d = 0
    for (v, v2) in zip(subset, subset[1:]):
        d += dists[v][R[v2]]
    if d < ans:
        ans = d
print(ans)
