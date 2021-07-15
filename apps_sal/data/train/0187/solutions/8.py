class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        op = 0
        profit = 0
        leftover = 0
        
        profmax = 0
        opmax = 0
        
        if 4 * boardingCost <= runningCost:
            return -1
        
        for n in customers:
            op += 1
            if n > 4:
                b = 4
                leftover += (n - 4)
            else:
                b = n
                if n + leftover > 4:
                    b = 4
                    leftover = leftover + n - 4
            profit += (boardingCost * b - runningCost)
            if (profit > profmax):
                profmax = profit
                opmax = op
        
        while leftover > 0:
            op += 1
            if leftover > 4:
                profit += (boardingCost * 4 - runningCost)
                leftover -= 4
            else:
                profit += (boardingCost * leftover - runningCost)
                leftover = 0
            if (profit > profmax):
                profmax = profit
                opmax = op   
                
        if profmax <= 0:
            return -1
        else:
            return opmax

        
        
        

