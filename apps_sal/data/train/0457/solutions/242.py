class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for _ in range(amount + 2)]
        dp[amount + 1] = float('inf')
        dp[amount] = 0
        for i in range(amount - 1, -1, -1):
            s = float('inf')
            for c in coins:
                s = min(s, 1 + dp[min(c + i, amount + 1)])
            dp[i] = s
        if dp[0] == float('inf'):
            return -1
        return dp[0]
