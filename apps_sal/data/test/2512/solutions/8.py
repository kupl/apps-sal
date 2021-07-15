from numba import jit
import numpy as np

@jit
def main():
    R, C, K = map(int, input().split())
    v_list = np.zeros((R+2,C+2), np.int64)
    for i in range(K):
        r, c, v = map(int, input().split())
        v_list[r][c] = v
    dp = np.zeros((R+2,C+2,4), np.int64)

    for i in range(R+1):
        for j in range(C+1):
            for n in range(4):
                dp[i+1][j][n] = max(dp[i+1][j][n], dp[i][j][n])
                dp[i][j+1][n] = max(dp[i][j+1][n], dp[i][j][n])
                if n <= 2:
                    dp[i+1][j][n+1] = max(dp[i+1][j][3], dp[i][j][3] + v_list[i+1][j])
                    dp[i][j+1][n+1] = max(dp[i][j+1][n+1], dp[i][j][n] + v_list[i][j+1])
    return dp[R][C][3]

print(main())
