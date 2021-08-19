class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def valid(dis):
            prev = 0
            balls = 1
            for i in range(1, n):
                if position[i] - position[prev] >= dis:
                    balls += 1
                    prev = i
            return balls >= m
        (lo, hi) = (0, position[-1] - position[0])
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if valid(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
