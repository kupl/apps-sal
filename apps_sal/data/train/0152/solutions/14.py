import bisect
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def is_ok(x):
            cur = -x
            for i in range(m):
                j = bisect.bisect_left(position, cur+x)
                if 0 <= j < len(position):
                    cur = position[j]
                else:
                    return False
            else:
                return True
                    
            
        l = 0
        r = 10**18
        while l+1 < r:
            c = (l+r)//2
            if is_ok(c):
                l = c
            else:
                r = c
        return l

