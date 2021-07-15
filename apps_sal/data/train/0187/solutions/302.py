class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        nrounds = len(customers)
        waiting = customers[0]
        profit = []
        nturns = 1
        rev = 0
        while waiting>0 or nturns<(nrounds+1):
            boarding = min(waiting,4)
            rev = rev+boarding*boardingCost
            waiting = waiting-boarding
            if nturns<(nrounds):
                waiting = waiting+customers[nturns]
            profit.append(rev-runningCost*nturns)
            nturns = nturns+1
        maxprof = 0
        ind = 0
        for i,p in enumerate(profit):
            if p>maxprof:
                maxprof=p
                ind=i
        if not maxprof>0:
            return -1
        else:
            return ind+1
