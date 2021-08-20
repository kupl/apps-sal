import math


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min = math.inf
            for j in coins:
                if i - j >= 0 and dp[i - j] < min:
                    min = dp[i - j]
            dp[i] = min + 1
        return dp[-1] if dp[-1] != math.inf else -1
