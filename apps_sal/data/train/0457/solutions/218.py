class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]
        for cost in range(0, len(dp)):
            for coin in coins:
                if cost + coin > amount:
                    continue
                dp[cost + coin] = min(dp[cost + coin], dp[cost] + 1)
        if dp[-1] != float('inf'):
            return dp[-1]
        return -1
