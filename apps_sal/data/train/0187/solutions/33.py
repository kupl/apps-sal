class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait=0
        maxp=-1
        profit=0
        ans=-1
        for i in range(len(customers)):
            
            wait+=customers[i]
            if(wait>4):
                wait-=4
                profit+=4*boardingCost
                profit-=runningCost
            else:
                profit+=(wait*boardingCost)
                wait=0
                profit-=runningCost
            if(profit>maxp):
                ans=i+1
                maxp=(profit)
            
        i=len(customers)
        while(wait!=0):
            if(wait>4):
                wait-=4
                profit+=4*boardingCost
                profit-=runningCost
            else:
                profit+=(wait*boardingCost)
                wait=0
                profit-=runningCost
            if(profit>maxp):
                ans=i+1
                maxp=profit
        
            i+=1
        if(maxp<=0):
            return -1
        else:
            return ans
                

