class Solution:
    
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        
        if A > B:
            A, B = B, A
            
        if B % A == 0:
            return A * N % 1000000007
        
        for i in range(1,A+1):
            if B*i % A == 0:
                break
        
        LCM = B*i
        
        nAB = LCM // A + i - 1
        
        r = N // nAB
        
        N %= nAB
        
#         print(nAB,r,N)
        
        return (r * LCM + sorted(set([A*i for i in range(N+1)]) | set([B*i for i in range(N+1)]))[N]) % 1000000007
        

