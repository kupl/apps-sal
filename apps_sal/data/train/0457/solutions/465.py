class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        dp = [[float('INF') for i in range(amount + 1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0
        for i in range( 1,len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1]< 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min( dp[i-1][j], dp[i][j-coins[i-1]] + 1 )

        if dp[len(coins)][amount] == float('INF'):
            return -1
        else:
            return dp[len(coins)][amount]

