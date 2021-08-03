class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        ans, s, last = 0, 0, 0
        i = 1
        while i < n:
            df = A[i] - A[i - 1]
            if df == 0:
                ans = max(ans, i - s)
                s = i
            elif i > 1 and last * df >= 0:
                ans = max(ans, i - s)
                s = i - 1
            last = df
            i += 1
        return max(ans, i - s)
