class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (1, position[-1] - position[0] + 1)

        def isInvalid(val):
            ball = 1
            previous = position[0]
            for p in position:
                if p - previous < val:
                    continue
                ball += 1
                previous = p
            return ball < m
        while l < r:
            mid = l + (r - l) // 2
            if isInvalid(mid):
                r = mid
            else:
                l = mid + 1
        return l - 1
