class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        prevBoard,waitQ,i,MaxProf,res=0,customers[0],1,-float('inf'),0
        while waitQ>0 or i<len(customers):
            if waitQ>4:
                board=4
            else:
                board=waitQ
            waitQ-=board
            profit=(prevBoard+board)*boardingCost-(i)*runningCost
            #print(profit,i)
            if profit>MaxProf:
                MaxProf=profit
                res=i
            prevBoard+=board
            if i<len(customers):
                waitQ+=customers[i]
            i+=1
        return -1 if MaxProf<0 else res

