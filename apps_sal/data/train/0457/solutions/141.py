class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1000000000.0 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            k = 1000000000.0
            for c in coins:
                if i - c >= 0:
                    k = min(k, dp[i - c] + 1)
            if k != 1000000000.0:
                dp[i] = k
        return -1 if dp[amount] == 1000000000.0 else dp[amount]
