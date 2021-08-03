class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        boarded = 0
        rotation = 0
        profit = 0
        for customer in customers:
            waiting += customer
            if waiting > 4:
                boarded += 4
                waiting -= 4
                rotation += 1
            else:
                boarded += waiting
                waiting = 0
                rotation += 1
            profit = boarded * boardingCost - rotation * runningCost
        optimal_rotation = rotation
        while waiting > 0:
            if waiting >= 4:
                boarded += 4
                waiting -= 4
            else:
                boarded += waiting
                waiting = 0
            rotation += 1
            new_profit = boarded * boardingCost - rotation * runningCost
            if new_profit > profit:
                profit = new_profit
                optimal_rotation = rotation
        if profit > 0:
            return optimal_rotation
        return -1
