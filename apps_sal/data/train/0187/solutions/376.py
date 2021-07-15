class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        highest = waiting = profit = time = i = 0
        highest_time = -1
        while i < len(customers) or waiting:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            boarding = min(waiting, 4)
            waiting -= boarding
            profit += boarding * boardingCost - runningCost
            time += 1
            if profit > highest:
                highest_time = time
            highest = max(profit, highest)
            
        return -1 if highest <= 0 else highest_time
