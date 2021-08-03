class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(position, val, m):
            balls = 1
            prev = position[0]
            for i in range(1, len(position)):
                if (position[i] - prev) >= val:
                    prev = position[i]
                    balls += 1
            if balls >= m:
                return True
            return False

        position.sort()
        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = (hi + lo + 1) // 2
            if check(position, mid, m):
                lo = mid
            else:
                hi = mid - 1
        return lo
