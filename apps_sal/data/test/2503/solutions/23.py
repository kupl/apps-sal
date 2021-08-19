# python 3.4.3
import numpy as np
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


def sum2d(i1, j1, i2, j2):
    A[i1][j1] += 1
    A[i1][j2] -= 1
    A[i2][j1] -= 1
    A[i2][j2] += 1


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N, K = list(map(int, input().split()))
XYC = [list(input().split()) for _ in range(N)]

A = [[0 for _ in range(K * 2 + 1)] for _ in range(K * 2 + 1)]

for x, y, c in XYC:
    # 白はそのまま, 黒はx軸方向にKずらして白として扱う
    i = (int(x) if c == "W" else int(x) + K) % (K * 2)
    j = int(y) % (K * 2)
    i0 = i % K
    j0 = j % K

    # 分割区画の左下が白の場合 (白は5箇所)
    #   a * b
    #   * c *
    #   d * e
    if (i < K and j < K) or (i >= K and j >= K):
        sum2d(0, 0, i0, j0)  # (a)左上
        sum2d(i0 + K, 0, K * 2, j0)  # (b)右上
        sum2d(i0, j0, i0 + K, j0 + K)  # (c)真ん中
        sum2d(0, j0 + K, i0, K * 2)  # (d)左下
        sum2d(i0 + K, j0 + K, K * 2, K * 2)  # (e)右下

    # 分割区画の左下が黒の場合 (白は4箇所)
    #   * a *
    #   b * c
    #   * d *
    else:
        sum2d(i0, 0, i0 + K, j0)  # (a)上
        sum2d(0, j0, i0, j0 + K)  # (b)左
        sum2d(i0 + K, j0, K * 2, j0 + K)  # (c)右
        sum2d(i0, j0 + K, i0 + K, K * 2)  # (d)下

# 2次元累積和
AA = np.array(A)
for i in range(K * 2):
    AA[i + 1, :] += AA[i, :]
for j in range(K * 2):
    AA[:, j + 1] += AA[:, j]

print((AA.max()))
