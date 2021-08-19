class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or len(coins) == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]
