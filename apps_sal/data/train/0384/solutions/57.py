class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10**9 + 7
        A.sort()
        n = len(A)
        ans = 0
        def exp(n):
            res = 1
            x = 2
            while n:
                if n&1:
                    res = (res*x)%mod
                n = n>>1
                x = (x*x)%mod
            
            return res
    
        for i in range(n):
            ans = (ans + exp(i)*A[i] - exp(n - i - 1)*A[i] + mod) % mod
        
        return ans
