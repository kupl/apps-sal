class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        prices.insert(0, 0)
        prices.insert(0, 0)
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[2] = -prices[2]

        for i in range(3, len(prices)):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        return sell[-1]
