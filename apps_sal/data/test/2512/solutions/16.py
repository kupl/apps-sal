import numpy as np
from numba import jit
(R, C, K) = list(map(int, input().split()))
G = np.zeros((R + 1, C + 1), np.int64)
for i in range(K):
    [r, c, v] = list(map(int, input().split()))
    G[r - 1][c - 1] = v


@jit
def main(G, R, C):
    dp = np.full((R + 1, C + 1, 4), -1)
    dp[0][0][0] = 0
    if G[0][0] != None:
        dp[0][0][1] = G[0][0]
    for r in range(R):
        for c in range(C):
            for k in range(4):
                if dp[r][c][k] == -1:
                    continue
                if k < 3:
                    if dp[r][c + 1][k + 1] < dp[r][c][k] + G[r][c + 1]:
                        dp[r][c + 1][k + 1] = dp[r][c][k] + G[r][c + 1]
                if dp[r][c + 1][k] < dp[r][c][k]:
                    dp[r][c + 1][k] = dp[r][c][k]
                if dp[r + 1][c][0] < dp[r][c][k]:
                    dp[r + 1][c][0] = dp[r][c][k]
                if dp[r + 1][c][1] < dp[r][c][k] + G[r + 1][c]:
                    dp[r + 1][c][1] = dp[r][c][k] + G[r + 1][c]
    return max(dp[r][c])


ret = main(G, R, C)
print(ret)
