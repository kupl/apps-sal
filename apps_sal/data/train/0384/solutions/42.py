class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        
        A = sorted(A)
        res = 0
        MOD = 10**9+7
        c = 1
        for i in range(len(A)):
            res = (res + A[i]*c%MOD)%MOD
            c <<= 1
            c %= MOD
        c = 1
        for i in range(len(A)-1, -1, -1):
            res = (res - A[i]*c%MOD)%MOD
            c <<= 1
            c %= MOD
        return (res+MOD)%MOD
            
            
        

