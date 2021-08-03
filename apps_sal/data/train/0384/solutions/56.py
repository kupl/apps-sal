class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10**9 + 7
        n = len(A)
        A.sort()
        ans = 0
        for i, v in enumerate(A):
            ans = (ans + (v << i) - (v << (n - 1 - i))) % mod
        return ans
