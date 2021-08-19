class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        mod = 10 ** 9 + 7
        (f, g) = (0, 0)
        ans = 0
        for i in range(1, len(A)):
            g = (2 * g + A[i - 1]) % mod
            f = (A[i] * ((1 << i) - 1) - g) % mod
            ans = (ans + f) % mod
        return ans
