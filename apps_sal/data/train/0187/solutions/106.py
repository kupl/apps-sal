class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        p=-1
        final=0
        ans=0
        s=0
        count=0
        for i in customers:
            s+=i
            if(s>4):
                ans+=4
                s-=4
            else:
                ans+=s
                s=0
            count+=1
            if(ans*boardingCost-count*runningCost)>final:
                p=count
                final=(ans*boardingCost-count*runningCost)
        while(s>0):
            if(s>4):
                ans+=4
                s-=4
            else:
                ans+=s
                s=0
            count+=1
            if(ans*boardingCost-count*runningCost)>final:
                p=count
                final=(ans*boardingCost-count*runningCost)
        return p
