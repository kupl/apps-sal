class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        res = 0
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + A[i]
        for i in range(0, n - L + 1):
            ls = psum[i + L] - psum[i]
            lm = max(self._max_m(0, i, M, psum), self._max_m(i + L, n, M, psum))
            res = max(res, ls + lm)
        return res

    def _max_m(self, s, e, M, psum):
        res = 0
        for i in range(s, e - M + 1):
            res = max(res, psum[i + M] - psum[i])
        return res
