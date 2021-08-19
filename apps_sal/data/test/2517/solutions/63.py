# coding: utf-8
from heapq import heappop, heappush
from itertools import permutations

N, M, R = map(int, input().split())
town = list(map(int, input().split()))
INF = 10**9
G = [[INF for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    A, B, C = map(int, input().split())
    G[A][B] = C
    G[B][A] = C

d = [[INF * 10 for i in range(N + 1)] for j in range(R)]

for k in range(R):
    r = town[k]
    d[k][r] = 0

    used = [False for i in range(N + 1)]

    heap = []
    heappush(heap, (d[k][r], r))

    while heap:
        d_u, u = heappop(heap)

        used[u] = True

        if d[k][u] < d_u:
            continue

        for v in range(N + 1):
            if not(used[v]) and d_u + G[u][v] < d[k][v]:
                d[k][v] = d_u + G[u][v]
                heappush(heap, (d[k][v], v))

ans = INF

L = [i for i in range(R)]

for v in permutations(L, R):
    D = 0
    for i in range(R - 1):
        D += d[v[i]][town[v[i + 1]]]
    ans = min(ans, D)

print(ans)
