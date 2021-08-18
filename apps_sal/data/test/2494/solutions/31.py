import itertools
from scipy.sparse import coo_matrix, lil_matrix
from scipy.sparse.csgraph import dijkstra, bellman_ford, floyd_warshall

N = int(input())

rows = []
cols = []
weights = []

"""
for _ in range(M):
    u, v, a = [int(i) for i in input().split()]
    rows.append(u-1)
    cols.append(v-1)
    weights.append(a)
"""

for i in range(N):
    rows.append(i)
    cols.append((i + 1) % N)
    weights.append(1)

for i in range(N):
    if i - ((10 * i) % N) == -1:
        weights[i] = 0
    elif i == N - 1 and i - ((10 * i) % N) == 1:
        weights[i] = 0
    else:
        rows.append(i)
        cols.append((10 * i) % N)
        weights.append(0)

graph = coo_matrix((weights, (rows, cols)), shape=(N, N)).tocsr()
d1 = dijkstra(graph, indices=1, directed=True, unweighted=False)

print((int(d1[0] + 1.5)))
