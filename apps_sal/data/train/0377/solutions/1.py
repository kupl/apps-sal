class Solution:
    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x * y // self.gcd(x, y)

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        AB = self.lcm(A, B)

        def check(mid):
            ans = mid // A + mid // B - mid // (AB)
            return ans >= N

        lo, hi = 0, N * A
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        mod = 10**9 + 7
        return lo % mod
