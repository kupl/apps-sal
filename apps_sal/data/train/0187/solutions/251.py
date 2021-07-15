class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        ans = []
        wait = 0
        onboard = 0
        i = 0
        while i<len(customers):
            wait += customers[i]
            onboard += min(4, wait)
            wait -= 4
            if wait<0:
                wait = 0
            
            ans.append((boardingCost * onboard) - (runningCost*(i+1)))
            i+=1
        
        while wait:
            onboard += min(4, wait)
            wait -= 4
            if wait<0:
                wait = 0
            
            ans.append((boardingCost * onboard) - (runningCost*(i+1)))
            i+=1
        
        val = max(ans)
        if val<0:
            return -1
        else:
            return ans.index(val)+1
        
        
        

