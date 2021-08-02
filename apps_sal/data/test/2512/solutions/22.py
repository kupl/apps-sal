import sys
import numpy as np
from numba import njit

R, C, K = map(int, input().split())
item = np.zeros((R, C), np.int_)
for s in sys.stdin.readlines():
    r, c, v = map(int, s.split())
    item[r - 1, c - 1] = v


@njit
def solve(R, C, K, item):
    DP = np.zeros((R, C, 4), np.int_)

    DP[0][0][1] = item[0][0]

    for i in range(R):
        for j in range(C):
            for k in range(4):
                if i > 0:  # 前の行から
                    DP[i, j, 0] = max(DP[i, j, 0], max(DP[i - 1, j]))  # 取らない
                    DP[i, j, 1] = max(DP[i, j, 1], max(DP[i - 1, j]) + item[i, j])  # 取る

                if j > 0:  # 前の列から
                    DP[i, j, k] = max(DP[i, j, k], DP[i, j - 1, k])  # 取らない
                    if k >= 1:
                        DP[i, j, k] = max(DP[i, j, k], DP[i, j - 1, k - 1] + item[i, j])  # 取る

    print(max(DP[R - 1, C - 1]))


solve(R, C, K, item)
