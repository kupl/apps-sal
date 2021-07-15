class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        ans = -math.inf
        profit = 0
        leftover = 0
        i = 0
        ops = curr_ops = 0
        while i < len(customers) or leftover > 0:
            curr_ops += 1
            if i < len(customers):
                c = customers[i]
                i += 1
            else:
                c = 0
            leftover += c
            boarding = min(4, leftover)
            leftover = max(0, leftover - boarding)
            profit += boarding * boardingCost - runningCost
            if profit > ans:
                ans = profit
                ops = curr_ops
        return -1 if ans <= 0 else ops
