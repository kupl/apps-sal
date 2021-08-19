class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        tmax_profit = 0
        rmax_profits = [0] * len(prices)
        rmax = -1
        for ii in range(len(prices) - 2, -1, -1):
            if (prices[rmax] - prices[ii] > rmax_profits[ii + 1]):
                rmax_profits[ii] = prices[rmax] - prices[ii]
            else:
                rmax_profits[ii] = rmax_profits[ii + 1]
            if prices[ii] > prices[rmax]:
                rmax = ii
        #print("rmax profit = {}".format(rmax_profits))
        lmin = 0
        lmax_profit = 0
        for ii in range(1, len(prices)):
            profit = prices[ii] - prices[lmin]
            if profit > lmax_profit:
                lmax_profit = profit
            if prices[ii] < prices[lmin]:
                lmin = ii
            tprofit = lmax_profit
            if ii < len(prices) - 1:
                tprofit += rmax_profits[ii + 1]
            #print("ii = {}, rmax_profit = {}, lmax_profit = {}, tprofit = {}".format(ii, rmax_profits[ii], lmax_profit, tprofit))
            if tprofit > tmax_profit:
                tmax_profit = tprofit
        return tmax_profit if tmax_profit > 0 else 0
