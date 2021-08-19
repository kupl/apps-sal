class Solution:

    def minDays(self, A: List[int], m: int, k: int) -> int:
        if m * k > len(A):
            return -1

        def isit(d):
            b = m
            for (i, j) in itertools.groupby(A, key=lambda x: x <= d):
                l = sum((1 for _ in j))
                if i == True:
                    b -= l // k
            return b <= 0
        l = 0
        r = max(A) + 1
        while l < r:
            mid = (l + r) // 2
            if isit(mid):
                r = mid
            else:
                l = mid + 1
        return l
