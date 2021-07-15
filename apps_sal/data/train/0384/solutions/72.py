class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A = sorted(A)
        length = len(A)
        _sum = 0
        for i in range(length):
            _sum += A[i] * 2**i
        
        for i in range(length):
            _sum -= A[i] * 2**(length-i-1)
            
        return _sum % (10**9 + 7)
