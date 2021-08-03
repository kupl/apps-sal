class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins = [coin for coin in coins if coin <= amount]
        if not coins:
            return -1
        dp = [0 for i in range(amount + max(coins) + 10)]
        for coin in coins:
            dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if dp[i] >= 1:
                    if dp[i + coin] == 0:
                        dp[i + coin] = dp[i] + 1
                    else:
                        if dp[i] + 1 < dp[i + coin]:
                            dp[i + coin] = dp[i] + 1
        if not dp[amount]:
            return -1
        return dp[amount]
