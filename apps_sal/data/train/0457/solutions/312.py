class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        INT_MAX = sys.maxsize - 1
        for i in range(0, amount + 1):
            dp[0][i] = INT_MAX
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[-1][-1] >= INT_MAX:
            return -1
        return dp[-1][-1]
