class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            if coins[i] <= amount:
                dp[coins[i]] = 1
        for i in range(1, amount + 1):
            if dp[i] == -1:
                comparison = []
                for c in coins:
                    if i - c >= 0 and dp[i - c] != -1:
                        comparison.append(dp[i - c])
                if comparison:
                    dp[i] = min(comparison) + 1
        return dp[amount]
