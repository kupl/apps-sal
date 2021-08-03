from math import ceil


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        r = 0
        boarded = 0
        maxProfit = 0
        maxR = -1
        print(customers, boardingCost, runningCost)
        for i in range(len(customers) - 1):
            customers[i + 1] += customers[i] - 4 if customers[i] > 4 else 0
            r += 1
            boarded += min(customers[i], 4)
            profit = boarded * boardingCost - r * runningCost
            if profit > maxProfit:
                maxProfit = profit
                maxR = r
        r += ceil(customers[-1] / 4)
        boarded += customers[-1]
        if customers[-1] % 4 > 0 and (customers[-1] % 4) * boardingCost - runningCost <= 0:
            r -= 1
            boarded -= customers[-1] % 4
        profit = boarded * boardingCost - r * runningCost
        if profit > maxProfit:
            maxProfit = profit
            maxR = r
        return maxR if maxProfit > 0 else -1
