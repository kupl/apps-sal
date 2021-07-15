class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:
             return 0
         buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
         for p in prices:
             buy1 = max(buy1, -p)
             sell1 = max(sell1, buy1 + p)
             buy2 = max(buy2, sell1 - p)
             sell2 = max(sell2, buy2 + p)
         return sell2
