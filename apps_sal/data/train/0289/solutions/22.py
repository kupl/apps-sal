class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        m_res = [None for i in range(len(A) - M + 1)]
        m = 0
        for i in range(len(A) - L + 1):
            ts = sum(A[i:i + L])
            for j in range(len(A) - M + 1):
                if j + M <= i or j >= i + L:
                    if m_res[j] is None:
                        m_res[j] = sum(A[j:j + M])
                    m = max(m, ts + m_res[j])
        return m
