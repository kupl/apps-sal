class Solution:

    def numSquares(self, n):
        import math

        def is_square(m):
            sqrt_m = int(math.sqrt(m))
            return sqrt_m * sqrt_m == m
        if is_square(n):
            return 1
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if is_square(n - i * i):
                return 2
        return 3
