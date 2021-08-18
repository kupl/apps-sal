class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for partial_amount in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= partial_amount:
                    dp[partial_amount] = min(dp[partial_amount], dp[partial_amount - coins[j]] + 1)
        return dp[amount] if dp[amount] <= amount else -1
