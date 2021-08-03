class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * target for _ in range(d)]

        for i in range(d):
            for j in range(target):
                if i == 0 and j + 1 <= f:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                elif j >= i:
                    for k in range(1, f + 1):
                        if j - k >= 0:
                            dp[i][j] += dp[i - 1][j - k]

        # print(dp)
        return dp[d - 1][target - 1] % 1000000007
