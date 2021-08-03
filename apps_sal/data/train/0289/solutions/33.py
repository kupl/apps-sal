class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A:
            return 0

        n = len(A)

        m_sum = 0
        for i in range(n - L + 1):
            i_sum = sum(A[i:i + L])
            for j in range(i + L, n - M + 1):
                m_sum = max(m_sum, (i_sum + sum(A[j:j + M])))
            for j in range(i - M + 1):
                m_sum = max(m_sum, (i_sum + sum(A[j:j + M])))

        return m_sum
