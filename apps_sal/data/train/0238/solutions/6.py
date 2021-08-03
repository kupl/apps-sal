class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = []
        sell = []
        for i in range(2):
            buy.append(-float("inf"))
            sell.append(-float("inf"))

        for i in prices:
            for j in range(2):
                if j == 0:
                    buy[j] = max(buy[j], -i)
                    sell[j] = max(sell[j], i + buy[j])
                else:
                    buy[j] = max(buy[j], sell[j - 1] - i)
                    sell[j] = max(sell[j], i + buy[j])

        return sell[-1]
