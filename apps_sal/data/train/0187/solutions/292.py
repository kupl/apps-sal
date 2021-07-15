class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        round=0
        maxProfit=0
        maxRound=-1
        waiting=0
        # wheel=[0]*4
        # g0=g1=g2=g3=0
        profit=0
        i=0
        for c in customers:
            i+=1
            waiting+=c
            g=min(4,waiting)
            waiting-=g
            profit+=g*boardingCost-runningCost
            if profit>maxProfit:
                maxProfit=profit
                maxRound=i
            if waiting: customers+=[0]
            # print(i,' profit is ',profit)
        return maxRound
            

