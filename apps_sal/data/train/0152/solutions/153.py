class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # we will binary search for the result
        position.sort()

        # the minimum possible distance between balls is 1
        lo = 1
        # the maximum possible distance is the distance from the end to the start
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
