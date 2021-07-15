class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:return 0
         times,n = 2, len(prices)
         dp = [[0 for j in range(n)] for i in range(times)]
         buy_in = -prices[0]
         for i in range(1,n):
             dp[0][i] = max(dp[0][i-1], prices[i] + buy_in)
             buy_in = max(buy_in, -prices[i])
             
             
         
         for k in range(1,times):
             buy_in = -prices[0]
             for j in range(1,n):
                 dp[k][j] = max(buy_in + prices[j], dp[k][j-1])
                 buy_in = max(buy_in, dp[k-1][j] - prices[j])
         return dp[-1][-1]
