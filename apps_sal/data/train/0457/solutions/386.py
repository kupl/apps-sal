class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        two choices, take or dont take
        DP[i][j], i is index of coin, j is amount

        take:
            DP[i][j] = DP[i][j-coins[i]] + 1
        dont take:
            DP[i][j] = DP[i-1][j]

          0 1 2 3 4 5 6 7 8 9 10 11
        1 0 1 2 3 4 5 6 7 8 9 10 11
        2 0 1 1 2
        5    
        """
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
        for r in range(len(coins)):
            dp[r][0] = 0
        for r in range(len(coins)):
            for c in range(1, amount + 1):
                take = leave = float('inf')
                if c - coins[r] >= 0:
                    take = dp[r][c - coins[r]] + 1
                if r > 0:
                    leave = dp[r - 1][c]
                dp[r][c] = min(leave, take)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
