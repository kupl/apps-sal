class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a, b):
            return a*b//gcd(a, b)
        
        def count_ugly(N, a, b, c):
            ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
            abc = lcm(ab, c)
            return N//a+N//b+N//c-N//ab-N//ac-N//bc+N//abc
            
        s, e =1, 2*10**9
        while s<=e:
            m = s+(e-s)//2
            cnt = count_ugly(m, a, b, c)
            if cnt>=n:
                e = m-1
            else:
                s = m+1
                
        return s
        

