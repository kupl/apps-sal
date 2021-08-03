class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell_date = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            sell_date[i] = max(sell_date[i - 1], prices[i] - min_price)
            min_price = min(prices[i], min_price)

        max_price, profit = prices[-1], 0
        for i in range(len(prices) - 1, 0, -1):
            profit = max(profit, max_price - prices[i] + sell_date[i])
            max_price = max(max_price, prices[i])

        return profit
