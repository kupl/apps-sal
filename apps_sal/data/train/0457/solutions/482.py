import numpy as np
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maximum = amount + 1
        dp = np.full((maximum), maximum)
        dp[0] = 0
        for i in range(1, maximum):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        if dp[amount] > amount:
            return -1
        return dp[amount]
