class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = customers[0]
        res = 0
        i = 1
        rotation = 0
        max_profit = 0
        max_rotation = -1
        total = 0
        while i < len(customers) or waiting > 0:
            rotation += 1
            curr = min(4, waiting)
            waiting -= curr
            total += curr
            res = total * boardingCost - rotation * runningCost
            if i < len(customers):
                waiting += customers[i]
                i += 1
            if res > max_profit:
                max_rotation = rotation
                max_profit = res

        return max_rotation
