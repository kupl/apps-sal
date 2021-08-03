class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        n = len(A)
        l, r = 1, A[-1] - A[0]

        def get_m(d):
            res = 1
            i = 1
            prev = A[0]
            while i < n:
                if A[i] - prev >= d:
                    res += 1
                    prev = A[i]
                i += 1
            return res

        while l < r:
            mid = r - (r - l) // 2
            if get_m(mid) < m:
                r = mid - 1
            else:
                l = mid
        return l
