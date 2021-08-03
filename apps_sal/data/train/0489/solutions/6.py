class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        a = sorted(list(range(len(A))), key=lambda x: A[x])
        ans = 0
        m = float('inf')
        for i in a:
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
