class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for x in range(len(dp)):
            for coin in coins:
                if x < coin:
                    continue
                if dp[x - coin] + 1 < dp[x]:
                    dp[x] = dp[x - coin] + 1
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[x]
