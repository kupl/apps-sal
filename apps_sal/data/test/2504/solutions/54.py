from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np
import sys
input = sys.stdin.readline
(n, m, l) = map(int, input().split())


def make_d_matrix(n, m, directed=False):
    inf = 10 ** 13
    d = [[inf] * n for _ in range(n)]
    if directed:
        for _ in range(m):
            (a, b, c) = map(int, input().split())
            d[a - 1][b - 1] = c
    else:
        for _ in range(m):
            (a, b, c) = map(int, input().split())
            d[a - 1][b - 1] = c
            d[b - 1][a - 1] = c
    return d


d = make_d_matrix(n, m)
csr_graph = csr_matrix(d)
d1 = floyd_warshall(csr_graph, directed=False)
inf = 10 ** 3
for i in range(n):
    for j in range(n):
        d1[i][j] = 1 if d1[i][j] <= l else inf
csr_graph = csr_matrix(d1)
d2 = floyd_warshall(csr_graph, directed=False)
q = int(input())
for _ in range(q):
    (s, t) = map(int, input().split())
    tmp = d2[s - 1][t - 1]
    if tmp >= inf:
        print(-1)
    else:
        print(int(tmp - 1))
