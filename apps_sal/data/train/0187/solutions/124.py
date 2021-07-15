class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        m=0
        res=-1
        leftover=0
        profit=0
        i=0
        j=0
        while leftover>0 or i<len(customers):
            if i<len(customers):
                leftover+= customers[i]
                i+=1
            if leftover>=4:
                profit+=4*boardingCost
                leftover-=4
            else:
                profit+=leftover*boardingCost
                leftover=0
            profit-=runningCost
            if profit>m:
                res=j+1
                m=profit
            j+=1
            
        return res
            

