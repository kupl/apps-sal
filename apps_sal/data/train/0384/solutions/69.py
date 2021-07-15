class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        res = 0
        A.sort()
        for i in range(0, len(A)):
            res += A[i] * (2**i - 2**(len(A)-i-1))
        return res % (10**9+7)
            

