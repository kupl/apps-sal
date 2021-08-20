class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:

        def _get_max(lo, hi, flag):
            m = float('-inf')
            s = 0
            for i in range(lo, hi):
                s = max(s, 0) + flag * A[i]
                m = max(m, s)
            return m
        s = sum(A)
        return max(_get_max(0, len(A), 1), s + _get_max(0, len(A) - 1, -1), s + _get_max(1, len(A), -1))
