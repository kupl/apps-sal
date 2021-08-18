class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        min_v = -sys.maxsize
        buy1, buy2 = min_v, min_v
        sell1, sell2 = 0, 0
        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(sell1, buy1 + i)

            buy2 = max(buy2, sell1 - i)
            sell2 = max(sell2, buy2 + i)
        return sell2
