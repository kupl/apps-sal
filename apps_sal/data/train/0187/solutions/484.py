class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        # customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8
        # customers = [8,3], boardingCost = 5, runningCost = 6
        l=[]
        j=1
        total=0
        for i in customers:
            
            total+=i
            if total<4:
                profit = total *boardingCost - runningCost
                if not l:
                    l.append((profit,j))
                else:
                    l.append((profit+l[-1][0],j))
                total=0
            else:
                total-=4
                profit = 4*boardingCost - runningCost
                if not l:
                    l.append((profit,j))
                else:
                    l.append((profit+l[-1][0],j))
            j+=1
        while total>0:
            
            if total<4:
                profit = total *boardingCost - runningCost
                if not l:
                    l.append((profit,j))
                else:
                    l.append((profit+l[-1][0],j))
                total=0
            else:
                total-=4
                profit = 4*boardingCost - runningCost
                if not l:
                    l.append((profit,j))
                else:
                    l.append((profit+l[-1][0],j))
            j+=1
        
        
        res = sorted(l, key = lambda x: (-x[0],x[1]))
        
        return res[0][1] if res[0][0]>0 else -1
        
        
        
        
            

