from numpy import zeros, int64
from numba import njit
(R, C, K, *RCV) = map(int64, open(0).read().split())
V = zeros((R + 1, C + 1), int64)
for (r, c, v) in zip(*[iter(RCV)] * 3):
    V[r][c] = v


@njit
def main():
    dp = zeros((R + 1, C + 1, 4), int64)
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            vij = V[i][j]
            for k in range(4):
                dp[i][j][k] = max(dp[i][j - 1][k], dp[i - 1][j][3])
            for k in range(3, 0, -1):
                dp[i][j][k] = max(dp[i][j][k], vij + dp[i][j][k - 1])
    print(dp[R][C][3])


main()
