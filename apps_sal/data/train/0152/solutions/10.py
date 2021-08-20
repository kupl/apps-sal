class Solution:

    def maxDistance(self, A: List[int], m: int) -> int:
        n = len(A)
        A.sort()

        def count(d):
            (ans, curr) = (1, A[0])
            for i in range(1, n):
                if A[i] - curr >= d:
                    ans += 1
                    curr = A[i]
            return ans
        (l, r) = (0, A[-1] - A[0])
        while l < r:
            mid = (l + r + 1) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
