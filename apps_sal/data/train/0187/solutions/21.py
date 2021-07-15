import math
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        run_count = 0
        profit = 0
        max_profit = 0
        stop_run = 0
        
        for customer in customers:
            waiting += customer
            if waiting > 4:
                waiting -= 4
                profit += 4*boardingCost - runningCost
            else:
                profit += waiting*boardingCost - runningCost
                waiting = 0        
            run_count += 1
            
            if profit > max_profit:
                max_profit = profit
                max_run = run_count
        while waiting > 0:
            if waiting > 4:
                waiting -= 4
                profit += 4*boardingCost - runningCost
            else:
                profit += waiting*boardingCost - runningCost
                waiting = 0        
            run_count += 1
            
            if profit > max_profit:
                max_profit = profit
                max_run = run_count
                
        run_count += math.ceil(waiting/4)
        profit += waiting*boardingCost - math.ceil(waiting/4)*runningCost
        
        if max_profit > 0:
            return max_run
        else:
            return -1
            
            

