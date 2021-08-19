MOD = 1000000007


class Solution:
    def dieSimulator(self, n, rollMax):
        r = max(rollMax)
        dp = [[0] * (r + 1) for _ in range(6)]
        # dp[i][j] last roll was i and i was thrown j consecutive times
        for i in range(6):
            dp[i][1] = 1
        for _ in range(n - 1):
            tmp = [[0] * (r + 1) for _ in range(6)]
            for i in range(6):
                for j in range(6):
                    if i != j:
                        for k in range(rollMax[i] + 1):
                            tmp[j][1] += dp[i][k]
                    else:
                        for k in range(rollMax[i]):
                            tmp[j][k + 1] += dp[j][k]

            dp = tmp
        res = 0
        for j in range(6):
            for k in range(r + 1):
                res = (res + dp[j][k]) % MOD
        return res % MOD
