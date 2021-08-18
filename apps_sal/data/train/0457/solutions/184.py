class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount + 1):
                sameCoin = amount + 1
                if j - coin >= 0:
                    dp[j] = min(dp[j - coin] + 1, dp[j])

        return dp[amount] if dp[amount] != amount + 1 else -1
