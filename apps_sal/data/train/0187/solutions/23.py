class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        cur_profit = remainder_customers = steps = res = 0
        max_profit = -1
        for customer in customers:
            remainder_customers += customer
            if remainder_customers > 4:
                remainder_customers -= 4
                cur_profit += 4* boardingCost - runningCost 
            else:
                cur_profit += remainder_customers* boardingCost - runningCost 
                remainder_customers = 0
            steps += 1 
            
            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps
                
        while remainder_customers > 0:
            if remainder_customers > 4:
                remainder_customers -= 4
                cur_profit += 4* boardingCost - runningCost 
            else:
                cur_profit += remainder_customers* boardingCost - runningCost 
                remainder_customers = 0
            steps += 1 
            
            if cur_profit > max_profit:
                max_profit = cur_profit
                res = steps
            
        
       
        return -1 if max_profit < 0 else res

