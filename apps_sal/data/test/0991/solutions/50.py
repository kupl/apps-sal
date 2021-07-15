# coding: utf-8
import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 銀貨を何枚持っているかの状態数、N*2501の都市, dijkstra
N, M, S = lr()
limit = 2500
S = min(S, limit)
graph = [[] for _ in range((N+1) * (limit+1))]  # 1-indexed
for _ in range(M):
    u, v, a, b = lr()
    for x in range(a, limit+1):
        graph[u*(limit+1) + x].append(((v*(limit+1)+x-a), b))
        graph[v*(limit+1) + x].append(((u*(limit+1)+x-a), b))

for i in range(N):
    i += 1
    c, d = lr()
    for x in range(limit-c+1):
        graph[i*(limit+1) + x].append((i*(limit+1) + x + c, d))

def dijkstra(start):
    INF = 10 ** 15
    dist = [INF] * ((N+1) * (limit+1))
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, prev = heappop(que)
        if dist[prev] < d:
            continue
        for next, time in graph[prev]:
            d1 = d + time
            if dist[next] > d1:
                dist[next] = d1
                heappush(que, (d1, next))
    return dist

dist = dijkstra(1*(limit+1)+S)
for i in range(2, N+1):
    answer = min(dist[i*(limit+1):(i+1)*(limit+1)])
    print(answer)

