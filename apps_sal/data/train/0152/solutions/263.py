from functools import lru_cache
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]
        
        def can_place(mid): # mid is candidate for minimum magnetic force
            num_placed = 1
            prev = position[0]
            
            for num in position[1:]:
                if num - prev >= mid:
                    num_placed += 1
                    prev = num

            return num_placed >= m  
        
        left = 0
        right = position[-1] - position[0]
        
        res = 0
        while left < right:
            mid = (left + right) // 2

            if can_place(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1
        
            

