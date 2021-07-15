class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        y = 0
        n = 0
        m = -math.inf
        res = -1
        k = 0
        
        for x in customers:
            n += x
            y += min(n,4)*boardingCost-runningCost
            n-=min(n,4)
            k+=1
            
            if y>m:
                m = y
                res = k
            
        while n:
            
            y += min(n,4)*boardingCost-runningCost
            n-=min(n,4)
            k+=1
            if y>m:
                m = y
                res = k
                
       
        return res if m>0 else -1 

