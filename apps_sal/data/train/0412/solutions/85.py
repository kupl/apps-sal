class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for x in range(target + 1)] for y in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                total_sum = 0
                for k in range(1, f + 1):
                    if j - k >= 0:
                        total_sum += dp[i - 1][j - k]
                dp[i][j] = total_sum
        return dp[d][target] % (10**9 + 7)
