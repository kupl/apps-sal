class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_buy = [0] * len(prices)
        max_sell = [0] * len(prices)
        max_rest = [0] * len(prices)

        max_buy[0] = -prices[0]
        max_sell[0] = 0
        max_rest[0] = 0

        for i in range(1, len(prices)):
            max_buy[i] = max(max_rest[i - 1] - prices[i], max_buy[i - 1])
            max_sell[i] = max(max_buy[i - 1] + prices[i], max_sell[i - 1])
            max_rest[i] = max(max_sell[i - 1], max_rest[i - 1])

        return max(max_buy[-1], max_sell[-1], max_rest[-1])
