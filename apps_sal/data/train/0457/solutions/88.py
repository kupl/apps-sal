class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Max = float('inf')

        dp = [0] + [Max] * amount

        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else Max for c in coins) + 1
        return dp[amount] if dp[amount] != Max else - 1
