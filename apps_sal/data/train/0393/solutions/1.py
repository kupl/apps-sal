class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:     
        ab = a*b//math.gcd(a,b)
        bc = b*c//math.gcd(b,c)
        ca = a*c//math.gcd(c,a)
        abc = ab*c//math.gcd(ab,c)
        lo = 1
        hi = 2*10**9
        while lo < hi:
            m = (lo+hi) //2
            cnt = m//a + m//b + m//c - m//ab - m//bc - m//ca + m//abc
            if cnt < n:
                lo = m+1
            else:
                hi = m
        return lo
