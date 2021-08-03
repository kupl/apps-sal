class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount or not coins:
            return 0

        dp = [[math.inf for _ in range(amount + 1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 0

        for i in range(1, amount + 1):
            if coins[0] <= i:
                dp[0][i] = 1 + dp[0][i - coins[0]]
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                take, leave = math.inf, math.inf
                if coins[i] <= j:
                    take = 1 + dp[i][j - coins[i]]
                leave = dp[i - 1][j]
                dp[i][j] = min(take, leave)
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1
