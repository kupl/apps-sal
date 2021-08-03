class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)

        def check(d):
            i, b = 0, 1
            for j in range(1, n):
                if position[j] - position[i] >= d:
                    b += 1
                    i = j
            return b >= m

        position = sorted(position)
        lo, hi = 1, position[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
