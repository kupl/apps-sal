import itertools
import numpy as np
from networkx.utils import UnionFind

N, K = list(map(int, input().split()))
A = np.array([tuple(map(int, input().split())) for _ in range(N)])

MOD = 998244353
MAX = 50
factorial = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    factorial[i] = factorial[i - 1] * i % MOD

uf_row = UnionFind(list(range(N)))
for i, j in itertools.combinations(list(range(N)), 2):
    if np.all(A[:, i] + A[:, j] <= K):
        uf_row.union(i, j)
uf_col = UnionFind(list(range(N)))
for i, j in itertools.combinations(list(range(N)), 2):
    if np.all(A[i] + A[j] <= K):
        uf_col.union(i, j)

row_res = 1
for group in uf_row.to_sets():
    row_res = row_res * factorial[len(group)] % MOD
col_res = 1
for group in uf_col.to_sets():
    col_res = col_res * factorial[len(group)] % MOD

print((row_res * col_res % MOD))
