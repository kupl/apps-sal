class Solution:

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        (prevSell, sell, prevBuy, buy) = (0, 0, 0, -prices[0])
        for price in prices:
            prevBuy = buy
            buy = max(prevBuy, prevSell - price)
            prevSell = sell
            sell = max(prevSell, prevBuy + price)
        return sell
