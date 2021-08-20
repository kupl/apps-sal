class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def maxBalls(d):
            (count, p) = (0, -d)
            for x in position:
                if x - p >= d:
                    (count, p) = (count + 1, x)
            return count
        (l, r) = (0, max(position))
        while l < r:
            d = r - (r - l) // 2
            if maxBalls(d) >= m:
                l = d
            else:
                r = d - 1
        return l
