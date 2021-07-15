class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        s, max_dist = -1, 0
        n = len(seats)
        
        for e in range(n):
            if not seats[e]: continue 
                
            if s == -1:
                max_dist = max(max_dist, e)
            else:
                max_dist = max(max_dist, floor((e-s)/2))

            s = e
            
        if seats[n-1] == 0:
            max_dist = max(max_dist, n-1-s)
            
        return max_dist     

