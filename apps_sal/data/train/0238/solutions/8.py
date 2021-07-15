class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:
             return 0
         
         n = len(prices)
         
         sell1 = n * [0]
         hold1 = n * [0]
         sell2 = n * [0]
         hold2 = n * [0]
         
         hold1[0] = hold2[0] = -prices[0]
         
         for i in range(1, n):
             sell1[i] = max(sell1[i-1], prices[i] + hold1[i-1])
             hold1[i] = max(hold1[i-1],  -prices[i])
             sell2[i] = max(prices[i] + hold2[i-1], sell2[i-1] )
             hold2[i] = max(sell1[i-1] - prices[i], hold2[i-1])
             
         return sell2[n-1]
             

