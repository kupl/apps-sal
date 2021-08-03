class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0:
            return 0

        dp = [[0 for i in range(target + 1)] for i in range(d + 1)]

        for i in range(1, min(f + 1, target + 1)):
            dp[1][i] = 1

        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]

                        if dp[i][j] >= 1000000007:
                            dp[i][j] -= 1000000007

        return dp[d][target]
