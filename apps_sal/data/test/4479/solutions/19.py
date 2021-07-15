# 5:47 -> 5:50 slowwww
# Seems greedy: pick smallest number and flip it
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K:
            m = min(A)
            m_i = A.index(m)
            A[m_i] = -m
            K -= 1
        return sum(A)
