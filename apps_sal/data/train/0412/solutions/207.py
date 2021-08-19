class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for i in range(target + 1)] for j in range(d)]
        for i in range(d):
            for j in range(target + 1):
                if i == 0:
                    dp[i][j] = 1 if j >= 1 and j <= f else 0
                else:
                    for l in range(1, f + 1):
                        if j - l > 0:
                            dp[i][j] += dp[i - 1][j - l]
                            dp[i][j] %= mod
        print(dp)
        return dp[-1][-1]
