class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:
             return 0
         sell = hold = 0
         buy = -prices[0]
         
         for i in range(1, len(prices)):
             
             sell, hold, buy = max(buy + prices[i], 0), max(hold, sell), max(hold-prices[i], buy)
             
         return max(sell, hold)
