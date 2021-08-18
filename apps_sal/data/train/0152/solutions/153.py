class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        lo = 1
        hi = position[-1] - position[0]

        def isPossible(minDistance):
            remaining = m
            prev = float('-inf')
            for p in position:
                if p - prev >= minDistance:
                    prev = p
                    remaining -= 1
            return remaining < 1

        while lo < hi:
            mid = hi - ((hi - lo) >> 1)
            if isPossible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
