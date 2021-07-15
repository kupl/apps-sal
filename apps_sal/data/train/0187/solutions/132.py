from collections import deque

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        
        rotations = 0
        maxprofit = -1
        currprofit = 0
        nr = 0
        q = deque(customers)
        
        while q:
            currprofit -= runningCost
            nr += 1
            
            c = q.popleft()
            if c > 4:
                if q:
                    q[0] += c-4
                else:
                    q.append(c-4)
                c = 4
                
            currprofit += c * boardingCost
            if currprofit > maxprofit:
                maxprofit = currprofit
                rotations = nr
            
        return rotations if maxprofit > 0 else -1
            
            
            
            
        
        

