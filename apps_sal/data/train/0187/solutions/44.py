class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        high = -1
        max_profit = -1
        prev = 0
        count = 0
        served = 0
        for cust in customers:
            if cust >= 4:
                served += 4
                prev += cust - 4
            elif prev + cust >= 4:
                prev -= 4 - cust
                served += 4
            else:
                served += cust + prev
                prev = 0
            count += 1
            profit = served * boardingCost - count * runningCost
            if max_profit < profit:
                max_profit = profit
                high = count
        while prev > 0:
            if prev > 4:
                served += 4
                prev -= 4
            else:
                served += prev
                prev = 0
            count += 1
            profit = served * boardingCost - count * runningCost
            if max_profit < profit:
                max_profit = profit
                high = count
        if count == 0 or high == -1:
            return -1
        return high
