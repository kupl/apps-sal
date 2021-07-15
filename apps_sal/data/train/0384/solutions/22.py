class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        B = sorted(A)
        res = 0
        mod = 10**9 + 7
        for i in range(len(B)):
            res += B[i] * ((1 << i) - (1 << (len(B) - i - 1)))
        return res % mod
