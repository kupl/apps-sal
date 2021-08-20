class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def count(dist):
            (prev, balls) = (-1000000000.0, 0)
            for p in position:
                if p - prev >= dist:
                    balls += 1
                    if balls == m:
                        break
                    prev = p
            return balls
        position.sort()
        (l, r) = (1, position[-1])
        res = 0
        while l < r:
            mid = (l + r) // 2
            balls = count(mid)
            if balls == m:
                res = mid
                l = mid + 1
            else:
                r = mid
        return res
