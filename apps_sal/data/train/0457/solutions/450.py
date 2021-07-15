class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount + 1)
        for i in range(1, len(dp)):
            small = float('inf')
            for j in range(len(coins) - 1, -1, -1):
                if (i - coins[j] >= 0):
                    small = min(small, 1 + dp[i - coins[j]])
            dp[i] = small
        return dp[-1] if dp[-1] != float('inf') else -1
