class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [amount + 1 for i in range(amount)]
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i - c] + 1, dp[i])
        return dp[amount] if dp[amount] < amount + 1 else -1
