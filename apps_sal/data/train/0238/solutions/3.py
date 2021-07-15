class Solution:
     def maxProfit(self, prices, k = 2):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:
             return 0
         
         s1 = s2 = 0
         b1 = b2 = -1000000000
         
         for p in prices:
             b1 = max(b1, -p)
             s1 = max(s1, b1 + p)
             b2 = max(b2, s1 - p)
             s2 = max(s2, b2 + p)
         
         return s2

