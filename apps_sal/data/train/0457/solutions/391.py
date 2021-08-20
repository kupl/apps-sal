class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(n)]
        for j in range(amount + 1):
            dp[0][j] = -1 if j % coins[0] else j // coins[0]
        for i in range(1, n):
            for j in range(1, amount + 1):
                includeDenom = -1 if coins[i] > j else dp[i][j - coins[i]]
                excludeDenom = dp[i - 1][j]
                if includeDenom == -1 and excludeDenom == -1:
                    dp[i][j] = -1
                elif includeDenom == -1:
                    dp[i][j] = excludeDenom
                elif excludeDenom == -1:
                    dp[i][j] = includeDenom + 1
                else:
                    dp[i][j] = min(includeDenom + 1, excludeDenom)
        return dp[n - 1][amount]
