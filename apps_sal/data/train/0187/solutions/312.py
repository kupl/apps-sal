class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        maxProfit = 0
        ans = 0
        revenue = 0
        cost = 0
        
        for c in range(len(customers)):
            waiting+=customers[c]
            cost+=runningCost
            
            toBeBoarded=min(waiting,4)
            waiting-=toBeBoarded
            
            revenue += toBeBoarded*boardingCost 
            profit = revenue-cost
            
            if profit>maxProfit:
                maxProfit, ans = profit, c
                
        while(waiting!=0):
            c+=1
            cost+=runningCost
            
            toBeBoarded=min(waiting,4)
            waiting-=toBeBoarded
            
            revenue += toBeBoarded*boardingCost 
            profit = revenue-cost
            
            if profit>maxProfit:
                maxProfit, ans = profit, c
                
        return ans+1 if maxProfit>0 else -1
