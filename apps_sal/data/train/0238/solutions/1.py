class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)

        sell1 = 0
        sell2 = 0
        hold1 = -prices[0]
        hold2 = -prices[0]

        for i in range(1, n):
            sell2 = max(prices[i] + hold2, sell2)
            hold2 = max(sell1 - prices[i], hold2)
            sell1 = max(prices[i] + hold1, sell1)
            hold1 = max(-prices[i], hold1)

        return sell2
