#  --*-coding:utf-8-*--

import heapq

INF = float('inf')


def dijkstra(graph, st):
    n = len(graph)
    ds = [INF] * n
    ds[st] = 0
    prevs = [None] * n

    qs = [(0, st)]

    while len(qs) > 0:
        d, nodeId = heapq.heappop(qs)

        if d > ds[nodeId]:
            continue

        for destId, length in graph[nodeId]:
            d2 = d + length
            if ds[destId] > d2:
                ds[destId] = d2
                prevs[destId] = nodeId
                heapq.heappush(qs, (d2, destId))

    return (ds, prevs)


N, M = list(map(int, input().split()))
G = [[] for _ in range(N * 3)]

for _ in range(M):
    u, v = list(map(int, input().split()))

    for i in range(3):
        G[u * 3 - 3 + i].append((v * 3 - 3 + (i + 1) % 3, 1))


S, T = list(map(int, input().split()))
ds, prevs = dijkstra(G, S * 3 - 3)

ans = ds[T * 3 - 3]
print((ans // 3 if ans != INF else -1))
