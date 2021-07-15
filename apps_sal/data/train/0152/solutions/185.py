class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def distributable(n):
            pos = position.copy()
            balls = m
            while pos and balls:
                balls -= 1
                np = pos[-1] - n
                while pos and pos[-1] > np:
                    pos.pop()
            return not balls       
        position = sorted(position)
        lo, hi = 1, (position[-1] - position[0]) // (m -1) + 1
        ans = lo
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if distributable(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans        
