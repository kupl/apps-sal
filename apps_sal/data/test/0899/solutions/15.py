
from itertools import combinations
from collections import defaultdict
from scipy.sparse import csr_matrix

from scipy.sparse.csgraph import dijkstra
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def read_ints():
    return list(map(int, read().split()))


N, M = read_ints()
adj_mat = [[0] * N for _ in range(N)]
INF = 10 ** 9
edges = defaultdict(lambda: INF)
for _ in range(M):
    a, b, c = read_ints()
    a -= 1
    b -= 1
    adj_mat[a][b] = c
    adj_mat[b][a] = c
    edges[a, b] = c

adj_mat = csr_matrix(adj_mat, dtype='int')
D = dijkstra(adj_mat, directed=False)

edge_not_use = set()


for (i, j), e in list(edges.items()):
    for s in range(N):
        d = D[s, j]
        if d == D[s, i] + e or d == D[s, j] + e:
            break
    else:
        edge_not_use.add((i, j))


print((len(edge_not_use)))
