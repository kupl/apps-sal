import sys
input = sys.stdin.readline


def main():
    (N, M, K) = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    class Comb:

        def __init__(self, N):
            self.fac = [1] * (N + 1)
            for i in range(2, N + 1):
                self.fac[i] = self.fac[i - 1] * i % MOD

        def pow(self, a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % MOD
                a = a ** 2 % MOD
                b >>= 1
            return res

        def comb(self, n, r):
            if r < 0 or r > n:
                return 0
            return self.fac[n] * self.pow(self.fac[r], MOD - 2) % MOD * self.pow(self.fac[n - r], MOD - 2) % MOD

        def permutation(self, n, r):
            if r == 0:
                return 1
            return self.fac[n] * self.pow(self.fac[n - r], MOD - 2) % MOD
    comb = Comb(N * M - 2)
    ans = 0
    for i in range(M):
        ans += i * (M - i) * N ** 2
    for i in range(N):
        ans += i * (N - i) * M ** 2
    print(ans * comb.comb(N * M - 2, K - 2) % MOD)


def __starting_point():
    main()


__starting_point()
