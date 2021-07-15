from collections import defaultdict
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N=len(seats)
        front=defaultdict(int)
        hind=defaultdict(int)
            
        frontI=float('-inf')
        hindI=float('inf')
        for n in range(N):
            if seats[n]==1:
                frontI=n
            front[n]=frontI
        for n in range(N)[::-1]:
            if seats[n]==1:
                 hindI=n
            hind[n]=hindI
        res=0  

        for n in range(N):
            if seats[n]==0:
                res=max(res, min(n-front[n],hind[n]-n))
        return res
                
            
            
            
        
        

        
        

