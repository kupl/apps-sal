from numba import jit
import numpy as np
import sys


def input():
    return sys.stdin.readline()[:-1]


@jit
def main():
    (R, C, K) = list(map(int, input().split()))
    item = np.zeros((R, C), np.int64)
    for i in range(K):
        (r, c, v) = list(map(int, input().split()))
        item[r - 1][c - 1] = v
    dp = np.zeros((R + 1, C + 1, 4), np.int64)
    for i in range(R):
        for j in range(C):
            for k in range(2, -1, -1):
                dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + item[i][j])
            for k in range(4):
                dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][k])
                dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
    return max(dp[R - 1][C - 1])


print(main())
