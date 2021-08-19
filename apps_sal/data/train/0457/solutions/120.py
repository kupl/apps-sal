class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * (amount)
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] = min(dp[j - c] + 1, dp[j])
        if dp[-1] != float('inf'):
            return dp[-1]
        return -1
    # Sanyam Rajpal
