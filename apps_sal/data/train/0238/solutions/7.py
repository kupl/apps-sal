class Solution:
    def maxProfit(self, prices):
        k = 2
        profit = []
        n = len(prices)
        if n < 2:
            return 0

        for i in range(k + 1):
            profit.append([])
            for j in range(n):
                profit[i].append(0)

        for i in range(1, k + 1):
            tmpMax = profit[i - 1][0] - prices[0]
            for j in range(n):
                profit[i][j] = max(profit[i][j - 1], prices[j] + tmpMax)
                tmpMax = max(tmpMax, profit[i - 1][j] - prices[j])
        return profit[k][n - 1]
