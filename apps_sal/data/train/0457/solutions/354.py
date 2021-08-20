class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        cl = len(coins)
        dp = [[math.inf for i in range(amount + 1)] for j in range(cl)]
        dp[0][0] = 0
        for i in range(1, amount + 1):
            if i - coins[0] >= 0:
                dp[0][i] = dp[0][i - coins[0]] + 1
        for i in range(1, cl):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j - coins[i] >= 0:
                    dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i][j])
        if dp[cl - 1][amount] == math.inf:
            return -1
        else:
            return dp[cl - 1][amount]
