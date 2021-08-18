class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [-1] * amount
        for x in range(amount + 1):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]
