class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        from fractions import gcd
        MOD = 10**9 + 7
        L = A / gcd(A, B) * B

        def max_unique_nums(x):
            return x // A + x // B - x // L

        lo = 0
        hi = N * min(A, B)
        while lo < hi:
            mid = (lo + hi) // 2
            if max_unique_nums(mid) < N:
                lo = mid + 1
            else:
                hi = mid
        return lo % MOD
