class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        positions = position
        positions.sort()
        n = len(positions)
        def f(d):
            prev = 0
            balls = 1
            for i in range(1, n):
                if positions[i] - positions[prev] >= d:
                    prev = i
                    balls += 1
                    if balls >= m:
                        return True
            return False
        lo, hi = 0, positions[-1] - positions[0]
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            if f(mi):
                lo = mi
            else:
                hi = mi - 1
        return lo
        
                    
            
            

