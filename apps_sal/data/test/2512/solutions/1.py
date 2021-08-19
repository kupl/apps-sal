import math
from numba import jit
import numpy as np


@jit
def solve():
    (r, c, k) = map(int, input().split())
    value = np.zeros((r, c), dtype=np.int64)
    for i in range(k):
        (r_t, c_t, v_t) = map(int, input().split())
        value[r_t - 1][c_t - 1] = v_t
    dp = np.zeros((r, c, 4), dtype=np.int64)
    dp[0][0][0] = 0
    for i in range(r):
        for j in range(c):
            for m in range(4):
                if i + 1 < r:
                    dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][m])
                if j + 1 < c:
                    dp[i][j + 1][m] = max(dp[i][j + 1][m], dp[i][j][m])
                if value[i][j] != 0 and m < 3:
                    if i + 1 < r:
                        dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][m] + value[i][j])
                    if j + 1 < c:
                        dp[i][j + 1][m + 1] = max(dp[i][j + 1][m + 1], dp[i][j][m] + value[i][j])
    for m in range(2, -1, -1):
        dp[r - 1][c - 1][m + 1] = max(dp[r - 1][c - 1][m + 1], dp[r - 1][c - 1][m] + value[r - 1][c - 1])
    return max(dp[r - 1][c - 1])


print(solve())
