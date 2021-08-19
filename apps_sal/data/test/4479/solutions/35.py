class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        if K == 0:
            return sum(A)
        m = min(A)
        m_i = A.index(m)
        A[m_i] = -m
        return self.largestSumAfterKNegations(A, K - 1)
