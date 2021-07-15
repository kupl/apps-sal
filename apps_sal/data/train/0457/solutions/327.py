class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for j in range(1,amount+1):
            dp[0][j] = float('inf')
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[len(coins)][amount] == float('inf'):
            return -1
        else:
            return dp[len(coins)][amount]
