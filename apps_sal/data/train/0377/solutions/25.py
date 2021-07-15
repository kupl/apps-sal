class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
        val = lcm(A, B)
        def number_magic_below(x):
            return x // A + x // B - x // val
        
        lo = min(A, B)
        hi = N * min(A, B)
        while lo < hi:
            mid = (lo + hi) // 2
            if number_magic_below(mid) < N:
                lo = mid + 1
            else:
                hi = mid
        return lo % (10**9 + 7)
