class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        res = 0
        mod = 10 ** 9 + 7
        N = len(A)
        for i in range(len(A)):
            res = (res + A[i] * 2 ** i - A[i] * 2 ** (N - i - 1)) % mod
        return res
