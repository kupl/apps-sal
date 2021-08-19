from itertools import permutations
from heapq import heappush, heappop
INF = 10 ** 12


def dijkstra(G, start=0, INF=INF):
    d = [INF for i in range(len(G))]
    d[start] = 0
    que = []
    heappush(que, (0, start))
    while len(que) != 0:
        p = heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for u in G[v].keys():
            if d[u] > d[v] + G[v][u]:
                d[u] = d[v] + G[v][u]
                heappush(que, (d[u], u))
    return d


(H, W) = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]
G = [{} for _ in range(10)]
for i in range(10):
    for j in range(10):
        G[i][j] = c[i][j]
dist = [0] * 10
for i in range(10):
    d = dijkstra(G, i)
    dist[i] = d[1]
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += dist[A[i][j]]
print(ans)
