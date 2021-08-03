class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[None for _ in range(d + 1)] for _ in range(target + 2)]
        for i in range(target + 2):
            dp[i][d] = 0
        dp[target][d] = 1
        for i in range(d + 1):
            dp[target + 1][i] = 0
        for i in range(target, -1, -1):
            for j in range(d - 1, -1, -1):
                s = 0
                for k in range(1, f + 1):
                    s += dp[min(i + k, target + 1)][j + 1] % 1000000007
                dp[i][j] = s
        return dp[0][0] % 1000000007
