class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        res = 0
        mod = 10 ** 9 + 7
        N = len(A)
        for i in range(len(A)):
            res += ((1 << i) - (1 << N - i - 1)) * A[i] % mod
        return res % mod
