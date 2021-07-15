class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        A.sort()
        n = len(A)
        return sum(a * ((1 << i) - (1 << n - i - 1)) for i, a in enumerate(A)) % mod
    
        # for i, a in enumerate(A):
        #     ans += a * ((1 << i) - (1 << n - i - 1)) % mod
        # return ans % mod

