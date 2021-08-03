class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        st_i = [a for a, _ in sorted(enumerate(A), key=lambda a: a[-1])]

        mi = math.inf
        mx = -math.inf

        for idx in st_i:
            mi = min(idx, mi)
            mx = max(mx, idx - mi)

        return mx
