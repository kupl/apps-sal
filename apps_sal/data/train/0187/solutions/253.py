class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if runningCost >= 4 * boardingCost:
            return -1
        prev = i = profit = rot = max_profit = min_rot = 0
        while i < len(customers) or prev:
            if i < len(customers):
                prev += customers[i]
            cur = min(4, prev)
            prev -= cur
            rot += 1
            profit += cur * boardingCost
            profit -= runningCost
            if profit > max_profit:
                min_rot = rot
                max_profit = profit
            i += 1
        if min_rot == 0:
            return -1
        return min_rot
