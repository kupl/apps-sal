class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         n = len(prices)
         if not n:
             return 0
         buys = [None] * n
         sells = [None] * n
         sells[0], buys[0] = 0, -prices[0]
         for x in range(1, n):
             delta = prices[x] - prices[x - 1]
             sells[x] = max(buys[x - 1] + prices[x], sells[x - 1] + delta)
             buys[x] = max(buys[x - 1] - delta, sells[x - 2] - prices[x] if x > 1 else -9999)
         return max(sells)

