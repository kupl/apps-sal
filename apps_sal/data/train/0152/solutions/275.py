class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        minp, maxp = position[0], position[-1]
        lo, hi = 1, (maxp - minp) // (m -1) + 1
        ans = lo
        def distributable(n):
            pos = position.copy()
            balls = m
            while pos and balls:
                balls -= 1
                np = pos[-1] - n
                while pos and pos[-1] > np:
                    pos.pop()
            return not balls       
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if distributable(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans        
