class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        from fractions import gcd
        MOD = 10**9 + 7

        L = A / gcd(A, B) * B
        M = L / A + L / B - 1
        q, r = divmod(N, M)

        if r == 0:
            return int(q * L) % MOD

        heads = [A, B]
        for _ in range(int(r) - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return int(q * L + min(heads)) % MOD
