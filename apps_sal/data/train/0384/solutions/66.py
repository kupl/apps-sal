class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        n = len(A)
        widthsum = 0
        mod = 10**9 + 7
        
        A.sort()
        
        p = s = 0
        pre, suf = [], []
        for i in range(n):
            p += A[i]
            s += A[-i-1]
            pre.append(p)
            suf.append(s)
            
        for l in range(n):
            widthsum += 2**(l)*(suf[l]-pre[l])
            widthsum %= mod
            
        return widthsum

