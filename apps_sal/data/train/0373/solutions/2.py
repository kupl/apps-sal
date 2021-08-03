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
                 3. When k is big enough to cover as many transactions as we want, 
                    use greedy algorithm (i.e. Stock Buy/Sell II)
         '''
        prices_length = len(prices)
        if prices_length == 0:
            return 0
        if k == 0:
            return 0

        # For N days, there will be at most N/2 transactions (N/2 buys and N/2 sells)
        # One buy + One sell = One transaction
        # When k is big enough to allow us buy/sell as many as we want, this becomes type-II
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
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

        # Generic solution
        candidate_max = float('-inf')
        profit = [0] * prices_length
        for trans in range(1, k + 1):

            cache = -prices[0]
            max_profit = 0
            for d in range(1, prices_length):
                if 2 * trans > d + 1:
                    continue  # For a given day, there are too many transaction allowed, no need to compute

                cache = -prices[d - 1] + profit[d - 1] if -prices[d - 1] + profit[d - 1] > cache else cache
                new_profit = prices[d] + cache

                # profit[d-1] has been used (the above line), now update it before 'max_profit' gets updated
                profit[d - 1] = max_profit

                max_profit = max_profit if max_profit > new_profit else new_profit

            # When loop ends, do one last update
            profit[-1] = max_profit
            candidate_max = profit[-1] if profit[-1] > candidate_max else candidate_max

        result = candidate_max if candidate_max > 0 else 0
        return result
