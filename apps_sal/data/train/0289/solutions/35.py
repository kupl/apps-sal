class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        max_sum = 0

        @lru_cache
        def _calculateSumFromIndex(i, length):
            return sum(A[i:i + length])

        for l in range(len(A) - L + 1):
            l_sum = _calculateSumFromIndex(l, L)
            if l >= M:
                for m in range(0, l - M + 1):
                    m_sum = _calculateSumFromIndex(m, M)
                    max_sum = max(max_sum, l_sum + m_sum)
            if len(A) - l + 1 >= M:
                for m in range(l + L, len(A) - M + 1):
                    m_sum = _calculateSumFromIndex(m, M)
                    max_sum = max(max_sum, l_sum + m_sum)
        return max_sum
