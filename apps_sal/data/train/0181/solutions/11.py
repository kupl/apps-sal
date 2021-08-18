class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.max_profit_rec(prices, {}, 0, 0)

    def max_profit_rec(self, prices, memo, idx, state):
        if idx >= len(prices):
            return 0
        if (idx, state) in memo:
            return memo[(idx, state)]
        memo[(idx, state)] = 0
        if state == 0:
            memo[(idx, state)] = max(self.max_profit_rec(prices, memo, idx + 1, 1) - prices[idx], self.max_profit_rec(prices, memo, idx + 1, 0))
        elif state == 1:
            memo[(idx, state)] = max(self.max_profit_rec(prices, memo, idx + 1, 2) + prices[idx], self.max_profit_rec(prices, memo, idx + 1, 1))
        else:
            memo[(idx, state)] = self.max_profit_rec(prices, memo, idx + 1, 0)
        return memo[(idx, state)]
