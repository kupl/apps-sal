import numpy as np
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
from scipy.sparse import csr_matrix

import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())

G = {}

for i in range(M):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, (-1) * (c - P)  # 最短炉問題にするため。
    if (a, b) in G and G[(a, b)] > c:
        G[(a, b)] = c
    elif (a, b) not in G:
        G[(a, b)] = c

A, B, C = [], [], []
for k, v in G.items():
    a, b = k
    c = v
    # G[a].append((b,c))
    A.append(a)
    B.append(b)
    C.append(c)

CC = [1] * len(A)
# https://atcoder.jp/contests/abc137/submissions/15987354
# とりあえず到達可能経路を探す、始点と終点から重み１にして辿っていき、双方登場した点が探すべき点。
# directedなので、A,Bを入れ替えているところもポイント
smat = bellman_ford(csr_matrix((CC, (A, B)), shape=(N, N)),
                    directed=True, unweighted=True, indices=0)
tmat = bellman_ford(csr_matrix((CC, (B, A)), shape=(N, N)),
                    directed=True, unweighted=True, indices=N - 1)
r = set([i for i, v in enumerate(smat + tmat) if not np.isinf(v)])
A, B, C = zip(*[(a, b, c) for a, b, c in zip(A, B, C) if b in r])
try:
    csr_mat = csr_matrix((C, (A, B)), shape=(N, N))
    #csr_mat.data = P - csr_mat.data
    x = -int(bellman_ford(csr_mat, directed=True, indices=0)[N - 1])
    if x < 0:
        x = 0
except NegativeCycleError:
    x = -1

print(x)
