class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):
            for value in coins:
                if i - value > 0:
                    if dp[i - value] >= 0:
                        if dp[i] < 0:
                            dp[i] = dp[i - value] + 1
                        else:
                            dp[i] = min(dp[i], dp[i - value] + 1)
                if i - value == 0:
                    dp[i] = 1
        return dp[amount]
