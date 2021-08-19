class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] + [0] * target for _ in range(d)]
        for i in range(d):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if k > j:
                        break
                    if i == 0:
                        dp[i][j] = int(j == k)
                    else:
                        dp[i][j] += dp[i - 1][j - k]
                    if dp[i][j] > 10 ** 9:
                        dp[i][j] = dp[i][j] % 10 ** 9 - 7 * (dp[i][j] // 10 ** 9)
        return dp[-1][-1]
