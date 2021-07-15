class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        B = sorted(A)
        res = 0
        mod = pow(10, 9) + 7
        for i in range(len(B)):
            res += B[i] * (pow(2, i) - pow(2, len(B) - i - 1))
        return res % mod
