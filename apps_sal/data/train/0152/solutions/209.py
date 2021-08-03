class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def is_possible(threshold):
            count = 0
            prev = -math.inf
            for x in position:
                if x - prev >= threshold:
                    count += 1
                    prev = x
            return count >= m

        span = position[-1] - position[0]
        lo, hi = 0, span
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
