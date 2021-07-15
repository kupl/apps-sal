class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        
        res = 0
        left = 0
        
        for i in range(len(customers)):
            customer = customers[i]
            left += customer
            
            if res <= i:
                if left < 4:
                    left = 0
                else:
                    left -= 4
                
                res += 1
            
            while left >= 4:
                res += 1
                left -= 4
                
                
        if left * boardingCost > runningCost:
            res += 1
                
        return res if res > 0 else -1
            
                
        
            
            

