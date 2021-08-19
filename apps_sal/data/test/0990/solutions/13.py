# 多分TLE
from scipy.sparse.csgraph import dijkstra
from itertools import combinations

N = int(input())
edge_id = {}
D = [[-float('inf')] * N for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    D[a - 1][b - 1] = D[b - 1][a - 1] = 1
    edge_id[(a - 1, b - 1)] = i
    edge_id[(b - 1, a - 1)] = i

paths = dijkstra(D, return_predecessors=True)[1]
M = int(input())
edges = [0] * M
for i in range(M):
    u, v = map(int, input().split())
    now, p = paths[u - 1][v - 1], v - 1
    edges[i] += 1 << edge_id[(now, p)]
    while now != u - 1:
        now, p = paths[u - 1][now], now
        edges[i] += 1 << edge_id[(now, p)]

ans = pow(2, N - 1)
coeff = -1
for m in range(1, M + 1):
    for comb in combinations(edges, m):
        e = 0
        for c in comb:
            e |= c
        ans += coeff * pow(2, N - 1 - bin(e).count('1'))
    coeff *= -1

print(ans)
