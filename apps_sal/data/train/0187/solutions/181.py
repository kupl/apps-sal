class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting=peak_at=peak=delta=profit=t=0
        while waiting or t<len(customers):
            if t < len(customers):
                waiting+=customers[t]
            t+=1
            delta =min(4,waiting)
            profit+=delta*boardingCost-runningCost
            waiting-=delta
            if peak<profit:
                peak=profit
                peak_at=t
        return peak_at if peak_at>0 else -1
                

