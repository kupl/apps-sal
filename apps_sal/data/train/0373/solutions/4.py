class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if k <= 0:
            return 0
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        buy = []
        sell = []
        for i in range(k):
            buy.append(-float("inf"))
            sell.append(-float("inf"))

        for i in prices:
            for j in range(k):
                if j == 0:
                    buy[j] = max(buy[j], -i)
                    sell[j] = max(sell[j], i + buy[j])
                else:
                    buy[j] = max(buy[j], sell[j - 1] - i)
                    sell[j] = max(sell[j], i + buy[j])

        return sell[-1]
