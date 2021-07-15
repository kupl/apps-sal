class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        i=0
        w=0
        c=0
        ans = 0
        fans = -1
        while(i<len(customers) or w):
            if i<len(customers):
                w+=customers[i]
            n = min(4,w)
            w-=n
            c+=n
            i+=1
            if ans < c*boardingCost - i*runningCost:
                ans = c*boardingCost - i*runningCost
                fans = i
        return fans
