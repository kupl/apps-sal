class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        idx = sorted(range(n), key=A.__getitem__)
        i = n
        result = 0
        for j in idx:
            result = max(result, j - i)
            i = min(i, j)
        return result
