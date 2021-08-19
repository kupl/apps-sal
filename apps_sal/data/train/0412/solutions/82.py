class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for x in range(d + 1)] for y in range(target + 1)]
        for i in range(1, min(f + 1, target + 1)):
            dp[i][1] = 1
        for i in range(1, target + 1):
            for j in range(2, d + 1):
                val = 0
                for k in range(1, f + 1):
                    if i - k >= 0:
                        val += dp[i - k][j - 1]
                dp[i][j] = val
        return dp[target][d] % (10 ** 9 + 7)
