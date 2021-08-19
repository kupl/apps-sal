class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[-1] > amount else dp[-1]
