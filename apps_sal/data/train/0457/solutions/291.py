class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        for j in range(amount + 1):
            dp.append(amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount + 1):
                sameCoin = float('inf')
                if j - coin >= 0:
                    sameCoin = dp[j - coin]
                dp[j] = min(sameCoin + 1, dp[j])
        return dp[j] if dp[j] != amount + 1 else -1
