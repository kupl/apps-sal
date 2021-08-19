class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        remain = 0
        for (i, v) in enumerate(customers):
            if remain + v > 4:
                customers[i] = 4
                remain = remain + v - 4
            else:
                customers[i] = remain + v
                remain = 0
        profits = [0] * len(customers)
        profits[0] = customers[0] * boardingCost - runningCost
        for i in range(1, len(customers)):
            profits[i] = profits[i - 1] + customers[i] * boardingCost - runningCost
        while remain > 0:
            if remain >= 4:
                profits.append(profits[-1] + 4 * boardingCost - runningCost)
                remain -= 4
            else:
                profits.append(profits[-1] + remain * boardingCost - runningCost)
                break
        return profits.index(max(profits)) + 1
