class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        r = -1
        maxV = 0
        pre = 0
        profit = 0
        i = 0
        while True:
            curr = 0
            if i < len(customers):
                curr = customers[i]
            profit += min(curr + pre, 4) * boardingCost - runningCost
            pre = max(curr + pre - 4, 0)
            if profit > maxV:
                r = i + 1
                maxV = profit
            i += 1
            if i >= len(customers) and pre <= 0:
                break
        return r
