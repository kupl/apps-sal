class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 16 < runningCost:
            return -1
        onboard = [0, 0, 0, 0]
        waiting = 0
        profits = []
        for i, grp in enumerate(customers):
            waiting += grp
            added = min(4, waiting)
            onboard[i % 4] = added
            waiting -= added
            profits.append(onboard[i % 4] * boardingCost - runningCost)
            i_last = i
        i = i_last + 1
        while waiting:
            added = min(4, waiting)
            onboard[i % 4] = added
            waiting -= added
            profits.append(onboard[i % 4] * boardingCost - runningCost)
            i += 1

        cum_sum = 0
        max_p = 0
        max_i = -1
        for i, prof in enumerate(profits):
            cum_sum += prof
            if cum_sum > max_p:
                max_p = cum_sum
                max_i = i + 1
        return max_i
