class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + ((1<<i) - (1<<(N-1-i))) * x) % MOD
        return ans        
