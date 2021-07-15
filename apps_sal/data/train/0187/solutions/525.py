class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans=[0]*1000000
        waiting=0
        for i in range(1000000):
            if i<len(customers):
                waiting+=customers[i]
            if waiting<=4:
                ans[i]=ans[i-1] + waiting*boardingCost - runningCost
                waiting=0
            else:
                ans[i]=ans[i-1] + 4*boardingCost -runningCost
                waiting-=4
            if waiting<=0 and i>=len(customers):
                break
        maxVal = max(ans)
        if maxVal<=0:
            return -1
        ret = ans.index(maxVal)+1
        return ret 
