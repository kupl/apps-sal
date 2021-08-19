class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        prefix = [0] * (n + 1)
        res = 0
        for i in range(0, n):
            prefix[i + 1] = prefix[i] + A[i]
        for i in range(0, n - L + 1):
            l_sum = prefix[i + L] - prefix[i]
            (j, m_sum) = (i, 0)
            while j - M >= 0:
                m_sum = max(m_sum, prefix[j] - prefix[j - M])
                j -= 1
            j = i + L
            while j + M <= n:
                m_sum = max(m_sum, prefix[j + M] - prefix[j])
                j += 1
            res = max(res, l_sum + m_sum)
        return res
