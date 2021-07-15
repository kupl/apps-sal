class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        
        pmax = 0
        pmax_ind = -1
        
        pcurr = 0
        
        for i, c in enumerate(customers):
            waiting += c
            spots = 4 
            
            
            while waiting > 0 and spots > 0:
                waiting -= 1
                spots -= 1
                
                pcurr += boardingCost
            
            pcurr -= runningCost
            
            if pcurr > pmax:
                pmax = pcurr
                pmax_ind = i
                
            
            # print(waiting, pmax,pmax_ind, pcurr)
            
        j = 0
        
        while waiting > 0:
            spots = 4
            
            j += 1
            
            while waiting > 0 and spots > 0:
                waiting -= 1
                spots -= 1
                
                pcurr += boardingCost
            
            pcurr -= runningCost
            
            # print(pmax, pmax_ind, pcurr)
            if pcurr > pmax:
                pmax = pcurr
                pmax_ind += j
                j = 0
                
                 
            
            
        
            
        return pmax_ind + 1 if pmax_ind != -1 else -1

