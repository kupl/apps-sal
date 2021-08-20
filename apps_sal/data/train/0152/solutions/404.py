class Solution:

    def maxDistance(self, position: List[int], k: int) -> int:
        position.sort()

        def check(m):
            prev = -1e+20
            c = 0
            for i in position:
                if i - prev >= m:
                    prev = i
                    c += 1
            return c >= k
        l = 0
        r = max(position)
        while l < r:
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else:
                r = m - 1
        return l
