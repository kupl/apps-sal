class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):

            for coin in coins:

                if 0 <= i - coin < amount + 1:

                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != sys.maxsize else -1
