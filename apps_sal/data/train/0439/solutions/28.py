class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        f0 = [0] * n
        f1 = [0] * n
        for k in range(n):
            f0[k] = max(1, f1[k - 1] + 1 if k >= 1 and A[k] < A[k - 1] else 0)
            f1[k] = max(1, f0[k - 1] + 1 if k >= 1 and A[k] > A[k - 1] else 0)
        return max(max(f0), max(f1))
