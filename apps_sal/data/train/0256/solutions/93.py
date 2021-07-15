class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        ceiling = lambda x,y : (x+y-1)//y

        def timeTaken(v):
            # total time taken if Koko eat with v speed
            totalTime = 0
            for p in piles: totalTime += ceiling(p, v)
            return totalTime
        
        def binarySearch(s, e, up_bound):
            # find maximum index that less or equal then up_bound, index s~e
            if(s == e): return s
            m = (s+e)//2
            if(timeTaken(m) <= up_bound):
                return binarySearch(s,m, up_bound)
            else: 
                return binarySearch(m+1, e, up_bound)   
        
        pmax = 1
        for p in piles: pmax = max(pmax, p)
        return binarySearch(1, pmax, H)
