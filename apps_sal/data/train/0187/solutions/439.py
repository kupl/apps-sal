class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        
        ans = 0
        anst = -1
        waiting = 0
        done = 0
        times = 0
        i = -1
        while waiting > 0 or i<len(customers):
            i+=1
            if i<len(customers):
                c = customers[i]
            else:
                c = 0
            times+=1
            waiting+=c
            done+=min(4,waiting)
            waiting-=min(4,waiting)
            tans = done*boardingCost-times*runningCost
            if tans>ans:
                ans = tans
                anst = times
            # print(waiting, i, c, tans, done, times)
            
        return anst
