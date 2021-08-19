class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:

        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)
        MOD = 10 ** 9 + 7
        L = A // gcd(A, B) * B
        M = L // A + L // B - 1
        (q, r) = divmod(N, M)
        if r == 0:
            return q * L % MOD
        increments = [A, B]
        for _ in range(r - 1):
            if increments[0] <= increments[1]:
                increments[0] += A
            else:
                increments[1] += B
        return (q * L + min(increments)) % MOD
