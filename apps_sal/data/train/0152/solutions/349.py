class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(dist):
            balls = m
            prev = None
            res = float('inf')
            for p in position:
                if prev is None or p - prev >= dist:
                    if prev:
                        res = min(res, p - prev)
                    prev = p
                    balls -= 1
            if balls > 0:
                return None
            return res
        (lo, hi) = (1, (position[-1] - position[0]) // (m - 1))
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            r = check(mid)
            if r:
                res = r
                lo = mid + 1
            else:
                hi = mid - 1
        return res
