class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        num_wait = 0
        num_rotate = 0
        num_served = 0
        max_profit = 0
        min_rotation = -1
        for c in customers:
            num_wait += c
            num_rotate += 1
            served = min(num_wait, 4)
            num_served += served
            num_wait -= served
            if boardingCost * num_served - runningCost * num_rotate > max_profit:
                min_rotation = num_rotate
            max_profit = max(max_profit, boardingCost * num_served - runningCost * num_rotate)
        while num_wait > 0:
            num_rotate += 1
            served = min(num_wait, 4)
            num_served += served
            num_wait -= served
            if boardingCost * num_served - runningCost * num_rotate > max_profit:
                min_rotation = num_rotate
            max_profit = max(max_profit, boardingCost * num_served - runningCost * num_rotate)
        if max_profit > 0:
            return min_rotation
        else:
            return -1
