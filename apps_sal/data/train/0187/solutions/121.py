class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting,prev_boarding,boarding,profit=0,0,0,[]
        for i, elem in enumerate(customers):
            if elem>=4:
                waiting+=elem-4
                boarding=4
            elif elem<4:
                if not waiting:
                    boarding=elem
                else:
                    boarding=4
                    waiting-=(4-elem)
            prev_boarding+=boarding
            profit.append(prev_boarding*boardingCost-((i+1)*runningCost))
        i=len(customers)
        while(waiting):
            if waiting>=4:
                boarding=4
                waiting-=4
                prev_boarding+=boarding
                i+=1
                profit.append(prev_boarding*boardingCost-((i)*runningCost))
            else:
                boarding=waiting
                waiting=0
                prev_boarding+=boarding
                i+=1
                profit.append(prev_boarding*boardingCost-((i)*runningCost))          
        return profit.index(max(profit))+1 if max(profit)>=0 else -1



