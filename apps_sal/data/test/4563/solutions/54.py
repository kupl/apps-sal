class Combination:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1 for i in range(self.n + 1)]
        self.finv = [1 for i in range(self.n + 1)]
        for i in range(2, self.n + 1):
            self.fac[i] = (self.fac[i - 1] * i) % self.mod
            self.finv[i] = (self.finv[i - 1] * pow(i, -1, self.mod)) % self.mod

    def comb(self, n, m):
        return self.fac[n] * (self.finv[n - m] * self.finv[m] % self.mod) % self.mod


def iparse():
    return list(map(int, input().split()))


def __starting_point():
    n = int(input())
    ml = 1
    last = [0, 0]
    for i in range(n):
        x = iparse()
        # print(len(x))
        l = (last[0] + x[0] - 1) // x[0]
        r = (last[1] + x[1] - 1) // x[1]
        m = max(l, r)
        if m == 0:
            m = 1
        x[0] *= m
        x[1] *= m

        last = x
    print((sum(last)))


__starting_point()
