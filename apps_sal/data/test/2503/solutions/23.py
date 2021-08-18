import numpy as np
import sys
input = sys.stdin.readline


def sum2d(i1, j1, i2, j2):
    A[i1][j1] += 1
    A[i1][j2] -= 1
    A[i2][j1] -= 1
    A[i2][j2] += 1


N, K = list(map(int, input().split()))
XYC = [list(input().split()) for _ in range(N)]

A = [[0 for _ in range(K * 2 + 1)] for _ in range(K * 2 + 1)]

for x, y, c in XYC:
    i = (int(x) if c == "W" else int(x) + K) % (K * 2)
    j = int(y) % (K * 2)
    i0 = i % K
    j0 = j % K

    if (i < K and j < K) or (i >= K and j >= K):
        sum2d(0, 0, i0, j0)
        sum2d(i0 + K, 0, K * 2, j0)
        sum2d(i0, j0, i0 + K, j0 + K)
        sum2d(0, j0 + K, i0, K * 2)
        sum2d(i0 + K, j0 + K, K * 2, K * 2)

    else:
        sum2d(i0, 0, i0 + K, j0)
        sum2d(0, j0, i0, j0 + K)
        sum2d(i0 + K, j0, K * 2, j0 + K)
        sum2d(i0, j0 + K, i0 + K, K * 2)

AA = np.array(A)
for i in range(K * 2):
    AA[i + 1, :] += AA[i, :]
for j in range(K * 2):
    AA[:, j + 1] += AA[:, j]

print((AA.max()))
