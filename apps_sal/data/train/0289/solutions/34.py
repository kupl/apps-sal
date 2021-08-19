class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        out = 0
        for i in range(n - L + 1):
            l = sum(A[i:i + L])
            m = [sum(A[j:j + M]) for j in range(i + L, n - M + 1)] + [sum(A[j:j + M]) for j in range(i - M)]
            if l and m:
                out = max(out, l + max(m))
        return out
