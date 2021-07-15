class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        profit = 0
        profits = []
        for i in range(len(customers)):
            waiting += customers[i]
            if waiting >= 4:
                waiting -= 4
                profit += boardingCost*4 - runningCost
            else:
                profit += boardingCost*waiting - runningCost
                waiting = 0
            profits.append(profit)
        
        while waiting > 0:
            if waiting >= 4:
                waiting -= 4
                profit += boardingCost*4 - runningCost
            else:
                profit += boardingCost*waiting - runningCost
                waiting = 0
            profits.append(profit)
            
        if max(profits) <= 0:
            return -1
        else:
            return profits.index(max(profits)) + 1    
