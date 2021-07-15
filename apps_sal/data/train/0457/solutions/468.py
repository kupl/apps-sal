import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[0 for i in range(amount+1)]for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if i==0:
                    dp[i][j]=sys.maxsize
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j%coins[0]==0:
                    dp[i][j]=j//coins[0]
                else:
                    dp[i][j]=sys.maxsize
        for i in range(2,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[len(coins)][amount]==sys.maxsize:
            return -1
        return dp[len(coins)][amount]

