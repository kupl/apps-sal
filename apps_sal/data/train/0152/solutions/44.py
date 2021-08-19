class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            (ans, curr) = (1, position[0])
            for i in range(1, n):
                if position[i] - curr >= d:
                    (curr, ans) = (position[i], ans + 1)
            return ans
        (l, r) = (0, position[-1] - position[0])
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

    def maxDistancwe(self, position: List[int], m: int) -> int:

        def count(mid):
            (r, c) = (1, position[0])
            for i in range(1, len(position)):
                if position[i] - c >= mid:
                    (c, r) = (position[i], r + 1)
            return r
        position.sort()
        (l, r) = (0, position[-1] - position[0])
        while l < r:
            mid = (r + l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
