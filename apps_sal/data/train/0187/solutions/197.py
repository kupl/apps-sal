class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        maxprofit = 0
        n = len(customers)
        if n == 0:
            return maxprofit

        waiting = customers[0]
        k = 1
        rounds = 1
        max_rounds = -1

        so_far = 0

        while k < n or waiting > 0:
            this_round = min(4, waiting)
            waiting -= this_round
            so_far += this_round
            profit = so_far * boardingCost - rounds * runningCost
            if profit > maxprofit:
                maxprofit = profit
                max_rounds = rounds
            if k < n:
                waiting += customers[k]
                k += 1

            rounds += 1

        return max_rounds
