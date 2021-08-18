class Factorials:
    def __init__(self, n, mod):
        self.mod = mod

        self.fac = [1]
        num = 1
        for i in range(1, n + 1):
            num *= i
            num %= mod
            self.fac.append(num)

        num = pow(num, mod - 2, mod)
        self.rec = [1 for i in range(n + 1)]
        self.rec[n] = num
        for i in range(n - 1, 0, -1):
            num *= i + 1
            num %= mod
            self.rec[i] = num

    def comb(self, n, r):
        return self.fac[n] * self.rec[r] * self.rec[n - r] % self.mod

    def perm(self, n, r):
        return self.fac[n] * self.rec[n - r] % self.mod


def main():
    n, m = map(int, input().split())
    mod = 10**9 + 7

    f = Factorials(m, mod)

    ans = 0
    for i in range(n + 1):
        if i % 2 == 0:
            ans += f.comb(n, i) * f.perm(m, i) * f.perm(m - i, n - i) * f.perm(m - i, n - i) % mod
        else:
            ans -= f.comb(n, i) * f.perm(m, i) * f.perm(m - i, n - i) * f.perm(m - i, n - i) % mod
        ans %= mod

    print(ans)


main()
