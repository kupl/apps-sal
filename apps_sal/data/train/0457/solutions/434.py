class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for c in range(1, len(dp)):
            dp[c][0] = 0
            for amt in range(1, len(dp[0])):
                if amt - coins[c - 1] >= 0:
                    dp[c][amt] = min(1 + dp[c][amt - coins[c - 1]], dp[c - 1][amt])
                else:
                    dp[c][amt] = dp[c - 1][amt]

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
