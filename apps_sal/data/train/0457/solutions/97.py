class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            if i - coins[-1] < 0:
                continue
            for coin in coins:
                index = i - coin
                if index >= 0 and dp[index] != -1:
                    value = dp[index] + 1
                    if dp[i] == -1 or dp[i] > value:
                        dp[i] = value
        return dp[amount]
