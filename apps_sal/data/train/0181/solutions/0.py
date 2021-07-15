class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         n = len(prices)
         
         if n < 2: return 0
         
         sells = [0] * n
         buys = [0] * n
         
         buys[0] = -prices[0]
         
         for i in range(1, n):
             sells[i] = max(sells[i-1], buys[i-1] + prices[i])
             buys[i] = max(buys[i-1], (sells[i-2] if i > 1 else 0) - prices[i])
             
         return sells[n-1]
