class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        '''
         https://www.youtube.com/watch?v=oDhu5uGq_ic
 
             i: number of transactions
             j: jth day 
 
             Total[i][j] = max(T[i][j-1], max((price[j] - price[m]) + T[i-1][m] for m in range(0, j-1)))
             
             NOTEs:
                 1. use cache
                 2. no need to initialize a 2D array, it takes too long
     
         '''
        prices_length = len(prices)
        if prices_length == 0:
            return 0
        if k == 0:
            return 0

        if 2 * k > (prices_length + 1):
            profit = 0
            max_price = prices[0]
            min_price = prices[0]

            for p in prices:
                if p < max_price:
                    profit += (max_price - min_price)
                    max_price = min_price = p
                else:
                    max_price = p

            profit += (max_price - min_price)

            return profit

        candidate_max = float('-inf')
        profit = [0] * prices_length
        for trans in range(1, k + 1):

            cache = -prices[0]
            max_profit = 0
            for d in range(1, prices_length):
                if 2 * trans > d + 1:
                    continue

                cache = -prices[d - 1] + profit[d - 1] if -prices[d - 1] + profit[d - 1] > cache else cache
                new_profit = prices[d] + cache

                profit[d - 1] = max_profit

                max_profit = max_profit if max_profit > new_profit else new_profit

            profit[-1] = max_profit
            candidate_max = profit[-1] if profit[-1] > candidate_max else candidate_max

        result = candidate_max if candidate_max > 0 else 0
        return result
