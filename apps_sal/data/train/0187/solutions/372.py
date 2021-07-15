class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        leftover = 0
        dp = [0]
        
        i=0
        while i<len(customers) or leftover:
            
            if i < len(customers):
                leftover += customers[i]
                
            newCust = min(4, leftover)
            leftover -= newCust
            
            temp = dp[-1] + newCust*boardingCost - runningCost
            dp.append(temp)
            
            i += 1
            
        if all([x<=0 for x in dp]):
            return -1
        return dp.index(max(dp))
