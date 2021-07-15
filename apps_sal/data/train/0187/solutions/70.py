class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        totpos = sum(customers)*boardingCost
        
        n = len(customers)
        currwaiting = 0
        rotat = 0
        i = 0
        imax = 0
        highestprof = -float('inf')
        gone = 0
        while currwaiting > 0 or i < n:
            if i < n:
                currwaiting += customers[i]
            # print(currwaiting)
            if currwaiting >= 4:
                currwaiting -= 4
                gone += 4
            else:
                gone += currwaiting
                currwaiting = 0
                
            
            # print(currwaiting)
                
            i += 1
            currprof = gone*boardingCost - i*runningCost
            # print(currprof)
            if currprof > highestprof:
                highestprof = currprof
                imax = i
            
        return imax if highestprof >= 0 else -1
                
            

