class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        N = len(A)
        if N==1: return 0
        MOD = 10**9 + 7
        A.sort()
        pow2 = [1]
        widths = 0
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)
            
        for i in range(N):
            widths = (widths + (pow2[i] - pow2[N-1-i]) * A[i]) % MOD
            
        return widths
