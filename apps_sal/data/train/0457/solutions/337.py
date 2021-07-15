class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = 0
            for j in range(1, amount + 1):
                dp[i][j] = min(dp[i - 1][j], (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else float('inf')) + 1)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
