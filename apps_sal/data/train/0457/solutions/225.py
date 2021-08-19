class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = float('inf')
            for c in coins:
                if c < i:
                    dp[i] = min(dp[i - c] + 1, dp[i])
                if c == i:
                    dp[i] = 1
        return dp[amount] if dp[amount] != float('inf') else -1
