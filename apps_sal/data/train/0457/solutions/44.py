class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('+inf')] * (amount + 1)
        dp[0] = 0

        for cnt in range(1, amount + 1):
            for coin in coins:
                if cnt - coin >= 0 and dp[cnt - coin] + 1 < dp[cnt]:
                    dp[cnt] = dp[cnt - coin] + 1

        if dp[amount] == float('+inf'):
            return -1

        return dp[amount]
