class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def validPlacement(spacing):
            placed, curPosition = 1, position[0]
            for p in position:
                if p - curPosition >= spacing:
                    placed += 1
                    curPosition = p
            return placed >= m

        position.sort()
        lo, hi = 0, position[-1] - position[0]
        while (lo < hi):
            mid = hi - (hi - lo) // 2
            if validPlacement(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
