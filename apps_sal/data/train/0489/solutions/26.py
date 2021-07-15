class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        res = 0
        m = float('inf')
        for i in sorted(list(range(len(A))), key=lambda x: A[x]):
            res = max(res, i - m)
            m = min(m, i)
        return res

