class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        A = sorted(A)
        if len(A) == 1:
            return 0
        lastaddon = 0
        lastv = 0
        for i in range(1, len(A)):
            lastaddon = 2 * lastaddon + (2 ** i - 1) * (A[i] - A[i - 1])
            lastv += lastaddon
        return lastv % MOD
