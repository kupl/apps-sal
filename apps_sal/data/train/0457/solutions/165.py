class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = min(f(amount-1), f(amount-2), f(amount-5))
        cap = amount + 1
        dp = [cap] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                dp[i] = min(dp[i - c] + 1 if i - c >= 0 else cap, dp[i])
        return dp[amount] if dp[amount] < cap else -1
