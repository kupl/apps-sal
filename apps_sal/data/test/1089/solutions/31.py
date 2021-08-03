import sys
input = sys.stdin.readline


class Comb:
    def __init__(self, n, mod=pow(10, 9) + 7, f=True, i=False):
        self.n = n
        self.mod = mod
        self.factorial_table = None
        self.inverse_table = None
        if f:
            self.get_factorial()
        if i:
            self.get_inverse()

    def get_factorial(self):
        self.factorial_table = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.factorial_table[i] = self.factorial_table[i - 1] * i % self.mod
        self.inverse_table = None

    def get_inverse(self):
        mod = self.mod
        self.inverse_table = [1] * (self.n + 1)
        for i in range(self.n + 1):
            self.inverse_table[i] = pow(self.factorial_table[i], -1, mod)

    def factorial(self, n):
        if self.factorial_table == None:
            return None
        return self.factorial_table[n]

    def inverse(self, n):
        if self.inverse_table == None:
            return None
        return self.inverse_table[n]

    def permutation(self, n, k):
        if self.factorial_table == None:
            return None
        mod = self.mod
        if self.inverse_table == None:
            return self.factorial_table[n] * pow(self.factorial_table[n - k], -1, mod) % mod
        return self.factorial_table[n] * self.inverse_table[n - k] % mod

    def comb(self, n, k):
        mod = self.mod
        if self.factorial_table == None:
            res = 1
            for i in range(k):
                res *= n - i
                res *= i + 1
                res %= mod
            return res
        if self.inverse_table == None:
            res = self.factorial_table[n] * pow(self.factorial_table[n - k], -1, mod) % mod\
                * pow(self.factorial_table[k], -1, mod) % mod
        else:
            res = self.factorial_table[n] * self.inverse_table[n - k] % mod\
                * self.inverse_table[k] % mod
        return res

    def recomb(self, n, k):
        if n + k - 1 > self.n:
            return None
        return self.comb(n + k - 1, k)


def main():
    n, m, k = list(map(int, input().split()))
    mod = pow(10, 9) + 7

    comb = Comb(n * m, i=True)

    ans = 0

    for i in range(n):
        ans += (i) * (n - i) * m**2
        ans %= mod

    for i in range(m):
        ans += (i) * (m - i) * n**2
        ans %= mod

    ans *= comb.comb(n * m - 2, k - 2)
    ans %= mod

    print(ans)


def __starting_point():
    main()


__starting_point()
