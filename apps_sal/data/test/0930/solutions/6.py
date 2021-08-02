import sys
input = lambda: sys.stdin.readline().rstrip()

mod = 10**9 + 7


class Mod:
    """
    comb = Mod(1000000)
    print(comb(5, 3))  # 5C3
    """

    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        self.modinv = self.__make_modinv_list(n_max)
        self.fac, self.facinv = self.__make_factorial_list(n_max)

    def comb(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def factorial(self, n):
        return self.fac[n]

    def factorial_inv(self, n):
        return self.facinv[n]

    def __make_factorial_list(self, n):
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return fac, facinv

    def __make_modinv_list(self, n):
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


def solve():

    n, k = list(map(int, input().split()))
    k = min(n - 1, k)
    m = Mod(n)

    ans = 0
    for i in range(k + 1):
        ans += m.comb(n - 1, n - 1 - i) * m.comb(n, i)
        ans %= mod

    print(ans)


def __starting_point():
    solve()


__starting_point()
