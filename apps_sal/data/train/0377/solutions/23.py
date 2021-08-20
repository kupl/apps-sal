class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        d = gcd(A, B)
        A //= d
        B //= d

        def how_many_below(n):
            return n // A + n // B - n // (A * B)
        lo = N - 1
        hi = min(A, B) * N
        while hi - lo > 1:
            h = (hi + lo) // 2
            if how_many_below(h) >= N:
                hi = h
            else:
                lo = h
        return hi * d % (10 ** 9 + 7)


def gcd(a, b):
    while a:
        (a, b) = (b % a, a)
    return b
