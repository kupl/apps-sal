class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        res = 0
        n = len(A)
        for i in range(n):
            res += A[i] * 2 ** i % 1000000007
            res -= A[i] * 2 ** (n - i - 1)
        return res % 1000000007
