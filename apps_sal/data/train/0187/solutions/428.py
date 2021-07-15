class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        maxi=-1
        n=len(customers)
        count=0
        spin=-1
        ride=0
        for i in range(n):
            count+=customers[i]
            
            ride+=min(4,count)
            pro=ride*boardingCost-(i+1)*runningCost
            
            if pro>maxi:
                maxi=pro
                spin=i+1
            count-=min(4,count)
        s=n
        while count>0:
            ride+=min(4,count)
            s+=1
            pro=ride*boardingCost-(s+1)*runningCost
            if pro>maxi:
                maxi=pro
                spin=s
            
            count-=min(4,count)
            
            
        return spin
            
            
            
            
            
            
        
            
        return spin
                
            
        
        

