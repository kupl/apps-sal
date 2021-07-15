class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        
        lo = 1
        hi = position[-1]
        
        while (lo < hi):
            mid = lo + (hi - lo) // 2 + 1
            
            if (self.can_be_put(position, m , mid)):
                lo = mid
            else:
                hi = mid - 1
                
        return lo
    
    def can_be_put(self, position, m, force):
        next_pos = position[0]
        
        for i in range(len(position)):
            if (next_pos <= position[i]):
                m -= 1
                next_pos = position[i] + force
                
        return m <= 0
