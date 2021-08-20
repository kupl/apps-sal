class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        start = 0
        position.sort()
        end = position[-1]

        def good(x):
            s = -1e+100
            count = 0
            for p in position:
                if p - s >= x:
                    count += 1
                    s = p
            return count >= m
        while start < end:
            mid = (start + end) // 2
            if good(mid + 1):
                start = mid + 1
            else:
                end = mid
        return start
