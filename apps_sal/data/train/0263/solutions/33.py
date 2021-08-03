class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 1000000007

        if N == 1:
            return 10

        a, b, c, d = 1, 1, 1, 1
        for _ in range(N - 1):
            a, b, c, d = (c + b) % MOD, (2 * a + d) % MOD, (2 * a) % MOD, (2 * b) % MOD

        return (4 * a + 2 * b + 2 * c + d) % MOD
