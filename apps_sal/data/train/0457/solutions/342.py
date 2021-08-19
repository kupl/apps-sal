class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(n)]
        for r in range(n):
            dp[r][0] = 0
        for a in range(1, amount + 1):
            (div, mod) = divmod(a, coins[0])
            if mod == 0:
                dp[0][a] = div
        for i in range(1, n):
            for a in range(1, amount + 1):
                if a - coins[i] >= 0:
                    dp[i][a] = min(dp[i][a - coins[i]] + 1, dp[i - 1][a])
                else:
                    dp[i][a] = dp[i - 1][a]
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
