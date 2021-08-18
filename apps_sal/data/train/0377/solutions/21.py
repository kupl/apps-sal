class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def compute_gcd(x, y):
            if y == 0:
                return x
            return compute_gcd(y, x % y)

        def compute_lcm(x, y):
            lcm = (x * y) // compute_gcd(x, y)
            return lcm

        C = compute_lcm(A, B)
        l = min(A, B)
        h = N * max(A, B)
        while (l < h):
            mid = (l + h) // 2
            m = mid // A + mid // B - mid // C
            if m >= N:
                h = mid
            else:
                l = mid + 1
        return l % (10**9 + 7)
