class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:

        def gcd(a, b):
            while b:
                (a, b) = (b, a % b)
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)
        val = lcm(A, B)
        magicals = set()
        for i in range(1, val // A + 1):
            magicals.add(i * A)
        for i in range(1, val // B + 1):
            magicals.add(i * B)
        sorted_magicals = sorted(magicals)
        return (sorted_magicals[(N - 1) % len(sorted_magicals)] + (N - 1) // len(sorted_magicals) * sorted_magicals[-1]) % (10 ** 9 + 7)
