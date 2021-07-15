class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rot=0
        profit=0
        
        maprof=0
        marot=0
        
        wait=0
        
        for c in customers:
            wait+=c
            
            if wait>4:
                wait-=4
                profit+=4*boardingCost - runningCost
            else:
                profit+=wait*boardingCost - runningCost
                wait=0
            rot+=1
            if profit>maprof:
                maprof=profit
                marot=rot
        while wait>0:
            if wait>4:
                wait-=4
                profit+=4*boardingCost - runningCost
            else:
                profit+=wait*boardingCost - runningCost
                wait=0
            rot+=1
            if profit>maprof:
                maprof=profit
                marot=rot
        if marot==0:
            marot=-1
        return marot
