class Solution:

    def maxProfit(self, prices):
        if not prices:
            return 0
        stock = -prices[0]
        noStock = 0
        noStockSell = 0
        for idx in range(len(prices)):
            price = prices[idx]
            print(noStock, stock, noStockSell)
            (noStock, stock, noStockSell) = [max(price + stock, noStock), max(noStockSell - price, stock), noStock]
        return noStock
