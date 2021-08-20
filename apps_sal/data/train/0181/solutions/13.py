class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free = 0
        (have, cool) = (float('-inf'), float('-inf'))
        for p in prices:
            (free, have, cool) = (max(free, cool), max(free - p, have), have + p)
        return max(free, cool)
