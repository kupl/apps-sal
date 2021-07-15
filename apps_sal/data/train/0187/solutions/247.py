class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        profit = -1
        served = 0
        wait = 0
        num_rotations = 0
        min_rotations = 0
        prev_profit = 0
        while(wait > 0 or num_rotations < n):
            i = customers[num_rotations] if num_rotations < n else 0
            wait += i
            if wait >= 4:
                wait = wait - 4
                served += 4
            else:
                served += wait
                wait = 0
            num_rotations += 1
            temp = served * boardingCost - num_rotations * runningCost
            profit = max(profit,temp)
            if profit == temp:
                min_rotations = min_rotations if prev_profit == profit else num_rotations
                prev_profit = profit
                
        if profit < 0:
            return -1
        return min_rotations
        

