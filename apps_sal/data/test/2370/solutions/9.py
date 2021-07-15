import sys

import numpy as np

sys.setrecursionlimit(10000)
INF = float('inf')

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

A = np.array(A, dtype=float)

useless = np.zeros((N, N), dtype=bool)
impossible = np.zeros((N, N), dtype=bool)
for via in range(N):
    # R[i][j]: i -> via -> j の距離
    R = sum(np.meshgrid(A[via], A[via]))
    R[via] = np.inf
    R[:, via] = np.inf
    useless |= R == A
    impossible |= R < A
if impossible.sum():
    print((-1))
else:
    print((int(A[~useless].sum() // 2)))

