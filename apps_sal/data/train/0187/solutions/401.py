class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        d={}
        k = 1
        curr = 0
        for ind,i in enumerate(customers):
            curr += i
            f = min(4,curr)
            d[k] = f
            k+=1
            curr -= f
        while(curr>0):
            d[k] = min(4,curr)
            curr-=min(4,curr)
            k+=1
        ans = []
        temp = 0
        for i in d:
            temp+=d[i]
            ans.append((temp*boardingCost)-(i*runningCost))
        res = ans.index(max(ans))+1
        if(max(ans)>=0):
            return res
        return -1
            
            
            

