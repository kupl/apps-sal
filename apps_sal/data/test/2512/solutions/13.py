import numpy as np
from numba import njit
(rr, cc, kk) = map(int, input().split())
goods = np.array([list(map(int, input().split())) for _ in range(kk)])
gg = np.zeros((rr, cc))
for (cr, ccc, ck) in goods:
    gg[cr - 1][ccc - 1] = ck


@njit
def calc(r, c, g):
    dp = -1 * np.ones((r + 1, c + 1, 4))
    maxlst = np.zeros((r + 1, c + 1))
    dp[:, 0, 0] = 0
    dp[0, :, 0] = 0
    for i in range(r):
        for j in range(c):
            tmp = 0
            for k in range(3):
                if g[i][j] > 0 and dp[i + 1][j][k] >= 0:
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j][k + 1], dp[i + 1][j][k] + g[i][j])
                else:
                    dp[i + 1][j + 1][k + 1] = dp[i + 1][j][k + 1]
                tmp = max(tmp, dp[i + 1][j + 1][k + 1])
            dp[i + 1][j + 1][0] = max(maxlst[i][j + 1], dp[i + 1][j][0])
            tmp = max(tmp, dp[i + 1][j + 1][0])
            if g[i][j] > 0 and dp[i + 1][j + 1][0] >= 0:
                dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i + 1][j + 1][0] + g[i][j])
                tmp = max(tmp, dp[i + 1][j + 1][1])
            maxlst[i + 1][j + 1] = tmp
    return maxlst[r][c]


print(int(calc(rr, cc, gg)))
