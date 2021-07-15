class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        max_profit = 0
        min_rot = 0
        gondolas = [0, 0, 0, 0]
        i = 0
        j = 1
        n_waiting = customers[0]
        while n_waiting or j < len(customers):
            if gondolas[i] > 0:
                gondolas[i] = 0
            if n_waiting <= 4:
                gondolas[i] = n_waiting
            else:
                gondolas[i] = 4
            n_waiting -= gondolas[i]    
            if j < len(customers):
                n_waiting += customers[j]
            profit += boardingCost*gondolas[i] - runningCost
            if profit > max_profit:
                min_rot = j
            max_profit = max(profit, max_profit)
            i += 1
            if i == 4:
                i = 0
            j += 1
            
        if max_profit:    
            return min_rot          
        return -1
        
                    
            

