class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(target + 1)] for i in range(d + 1)]
        dp[0][0] = 1
        for i in range(d):
            for ff in range(1, f + 1):
                for sm in range(target):
                    if sm + ff <= target:
                        dp[i + 1][sm + ff] += dp[i][sm]
        return dp[d][target] % (10 ** 9 + 7)
