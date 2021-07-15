class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        
        profits = [0]
        waiting = 0
        
        for customer in customers:
            waiting += customer
            serving = 0
            if waiting > 4:
                serving = 4
                waiting -=4
            else:
                serving = waiting
                waiting =0
                
            profits.append(profits[-1] + ((boardingCost*serving) - runningCost))
            
        while waiting:
            serving = 0
            if waiting > 4:
                serving = 4
                waiting -=4
            else:
                serving = waiting
                waiting =0
                
            profits.append(profits[-1] +  ((boardingCost*serving) - runningCost))
        
        maxProfit = profits[1]
        maxProfitIndex = 1
        for i, profit in enumerate(profits[1:]):
            if profit>maxProfit:
                maxProfit = profit
                maxProfitIndex = i+1
        
        if maxProfit>0:
            return maxProfitIndex
        else:
            return -1
        
        

