class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        nrot = 0
        i = 0
        profits = []
        if customers[i] > 0:
            waiting = customers[i] - min(4, customers[i])
            nrot += 1
            profits.append(min(customers[i], 4) * boardingCost - 1 * runningCost)
        else:
            waiting = 0
            profits.append(0)
        customers.append(0)
        while waiting > 0 or i <= len(customers):
            profits.append(profits[-1] + min(waiting, 4) * boardingCost - 1 * runningCost)
            if i + 1 <= len(customers) - 1:
                waiting += - min(4, waiting + customers[i + 1]) + customers[i + 1]
            else:
                waiting -= min(waiting, 4)
            nrot += 1
            i += 1
        mx = profits.index(max(profits))
        return mx + 1 if max(profits) > 0 else -1
