''''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] first i coins with sum of j
        # dp[i][j] = min(dp[i-1][j], dp[i][j-k]+1) for k in coins
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c]+1)
        return dp[-1] if dp[-1] < float('inf') else -1


        

'''    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] first j coins with sum of i
        # dp[i][j] = min(dp[j-coins[k][k]]+1) for k in coins
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount+1):
            for c in coins:
                if j >= c:
                    dp[j] = min(dp[j], dp[j-c]+1)
        return dp[-1] if dp[-1] < float('inf') else -1
