class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        buy, sell = [0] * n, [0] * n
        buy[0], buy[1] = -prices[0], -min(prices[0:2])
        sell[1] = max(0, buy[0] + prices[1])
        for i in range(2, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])

        return sell[-1]
