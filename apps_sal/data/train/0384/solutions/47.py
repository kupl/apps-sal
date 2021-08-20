class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        A.sort()
        B = [A[i] - A[n - i - 1] for i in range(n)]
        ans = 0
        for (i, v) in enumerate(B):
            ans = (ans + (v << i)) % mod
        return ans
