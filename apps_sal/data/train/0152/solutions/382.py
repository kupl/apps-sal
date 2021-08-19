class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]

        def count(dist):
            (prev, balls) = (position[0], 1)
            for p in position[1:]:
                if p - prev >= dist:
                    balls += 1
                    if balls == m:
                        break
                    prev = p
            return balls
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
