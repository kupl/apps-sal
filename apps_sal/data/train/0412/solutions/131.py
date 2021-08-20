class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(max(target + 1, f + 1))] for _ in range(d + 1)]
        for i in range(1, f + 1):
            dp[1][i] = 1
        for dice in range(1, d + 1):
            for values in range(1, target + 1):
                for i in range(1, f + 1):
                    if values - i < 1:
                        break
                    dp[dice][values] += dp[dice - 1][values - i]
        return dp[d][target] % (10 ** 9 + 7)
