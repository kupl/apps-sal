class Solution:

    def knightDialer(self, n: int) -> int:
        (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9) = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        mod = pow(10, 9) + 7
        for i in range(n - 1):
            t0 = (x4 + x6) % mod
            t1 = (x6 + x8) % mod
            t2 = (x7 + x9) % mod
            t3 = (x4 + x8) % mod
            t4 = (x0 + x3 + x9) % mod
            t5 = 0
            t6 = (x0 + x1 + x7) % mod
            t7 = (x2 + x6) % mod
            t8 = (x1 + x3) % mod
            t9 = (x2 + x4) % mod
            (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9) = (t0, t1, t2, t3, t4, t5, t6, t7, t8, t9)
        return (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) % mod
