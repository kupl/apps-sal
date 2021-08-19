class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        (ret, mod, p) = (0, 10 ** 9 + 7, 1)
        for i in range(len(A)):
            ret += (A[i] - A[len(A) - i - 1]) * p % mod
            p = (p << 1) % mod
        return ret % mod
