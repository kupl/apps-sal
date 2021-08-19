class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        max_profit = 0
        max_profit_count = 0
        rotation_count = 0
        waiting = 0
        i = 0
        while waiting or i < len(customers):
            if i < len(customers):
                customer = customers[i]
                i += 1
                waiting += customer
            if waiting:
                boarded = 4
                if waiting < 4:
                    boarded = waiting
                waiting -= boarded
                profit += boarded * boardingCost
            rotation_count += 1
            profit -= runningCost
            if profit > max_profit:
                max_profit = profit
                max_profit_count = rotation_count
        if profit > 0:
            return max_profit_count
        else:
            return -1
