class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def possible(force):
            prev = float('-inf')
            balls_placed = 0
            for x in position:
                if x-prev >= force:  # then that means we have that required force and we can keep a new ball here at position x
                    prev= x
                    balls_placed+=1  
                
            return(balls_placed>=m)
        
        lo,hi = 0, max(position)
        while lo<hi:
            mid = (lo+hi+1)//2
            if possible(mid):
                lo=mid
                
            else:
                hi=mid-1
                
        return(lo)
