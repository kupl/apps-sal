class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for n in coins:
                if i - n >= 0 and dp[i - n] + 1 < dp[i]:
                    dp[i] = dp[i - n] + 1
        return dp[-1] if dp[-1] != amount + 1 else -1
