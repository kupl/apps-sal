import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

input = sys.stdin.readline


N, M, S = map(int, input().split())
S = min(S, 2500)

row = []
col = []
data = []

for _ in range(M):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    for i in range(a, 2501):
        row.append(N * i + u)
        col.append(N * (i - a) + v)
        data.append(b)
        row.append(N * i + v)
        col.append(N * (i - a) + u)
        data.append(b)

for u in range(N):
    c, d = map(int, input().split())
    for i in range(1, c):
        row.append(N * (2500 - i) + u)
        col.append(N * 2500 + u)
        data.append(d)
    for i in range(c, 2501):
        row.append(N * (i - c) + u)
        col.append(N * i + u)
        data.append(d)

graph = csr_matrix((data, (row, col)), shape=(2501 * N, 2501 * N))

times = dijkstra(graph, directed=True, indices=N * S)

for end in range(1, N):
    print(int(min(times[N * i + end] for i in range(2501))))
