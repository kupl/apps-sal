class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        def fn(k):
            return k//a + k//b + k//c - k//ab - k//bc - k//ca + k//abc

        lo, hi = 0, 2_000_000_000
        while lo < hi:
            mid = (lo + hi)//2
            if fn(mid) >= n: hi = mid
            else: lo = mid + 1
        return lo
