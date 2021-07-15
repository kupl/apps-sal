class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        LCM = A*B//gcd(A, B)
        m = LCM//A + LCM//B -1
        q, r = divmod(N, m)
        if r==0:
            return q*LCM%(10**9+7)
        # print(q, r, m, LCM)
        pa, pb = 0, 0
        for _ in range(r):
            nxt = min(A*(pa+1), B*(pb+1))
            if nxt==A*(pa+1):
                pa += 1
            if nxt==B*(pb+1):
                pb += 1
        
        return (q*LCM+nxt)%(10**9+7)
            
            
        
        

