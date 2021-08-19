class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(position, d, m):
            last = position[0]
            balls = m - 1
            i = 1
            while balls and i < len(position):
                if position[i] - last < d:
                    i += 1
                else:
                    last = position[i]
                    balls -= 1
            return balls == 0
        position.sort()
        hi = position[-1]
        lo = 1
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if check(position, mi, m):
                lo = mi
            else:
                hi = mi - 1
        return lo
