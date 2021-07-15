class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        current = 0
        profit = 0
        times = -1
        waitings = 0
        
        for index in range(0, len(customers)):
            waitings += customers[index]
            
            current -= runningCost
            current += (boardingCost * min(waitings, 4))
            
            waitings -= min(waitings, 4)
            
            if current > profit:
                times = index + 1
                profit = current
        
        index = len(customers)
        while waitings > 0:
            current -= runningCost
            current += (boardingCost * min(waitings, 4))
            
            waitings -= min(waitings, 4)
            
            if current > profit:
                times = index + 1
                profit = current
            
            index += 1
        
        
        return times
        

