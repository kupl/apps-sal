class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def can_place(force):
            count = 1
            curr = position[0]
            for i in range(1, len(position)):
                if position[i] - curr >= force:
                    count += 1
                    curr = position[i]
            return count
        
        position.sort()
        
        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        return lo
