class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()

        def possible(force):
            placed = 0
            pos = -math.inf

            for p in positions:
                if p - pos >= force:
                    placed += 1
                    pos = p

            return placed >= m

        (lo, hi) = (0, positions[-1])

        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
