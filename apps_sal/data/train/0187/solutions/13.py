class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        
        n = len(customers)
        
        profit = 0
        maxProfit = 0
        rotation = 0
        optRotation = -1
        
        waiting = 0
        
        for i in range(n):
            customer = customers[i] + waiting
            if customer > 3:
                profit += 4 * boardingCost - runningCost
                waiting = customer - 4
                rotation += 1
            else:
                profit += customer * boardingCost - runningCost
                waiting = 0
                rotation += 1
            
            if profit > maxProfit:
                maxProfit = profit
                optRotation = rotation
            
        if waiting > 0:
            lastRotations = waiting // 4
            lastCustomers = waiting % 4
            profit += (4 * boardingCost - runningCost) * lastRotations
            rotation += lastRotations
            
            if profit > maxProfit:
                maxProfit = profit
                optRotation = rotation
                
            if lastCustomers != 0:
                profit += lastCustomers * boardingCost - runningCost
                rotation += 1
            
            if profit > maxProfit:
                maxProfit = profit
                optRotation = rotation
        
        return optRotation
