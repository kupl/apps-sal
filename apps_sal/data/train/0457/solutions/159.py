class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 10
        dp = [MAX for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            curr = i
            for coin in coins:
                prev = curr - coin
                if prev >= 0:
                    dp[curr] = min(dp[curr], dp[prev] + 1)

        return dp[amount] if dp[amount] != MAX else -1
