class nCrMod():
    def __init__(self, mod):
        self.mod = mod
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]

    def prep(self, n):
        mod = self.mod
        f, fi = self.fac[-1], self.finv[-1]
        for i in range(len(self.fac), n + 1):
            fn = f * i % mod
            v = -self.inv[mod % i] * (mod // i) % mod
            fin = fi * v % mod
            f, fi = fn, fin
            self.fac.append(f)
            self.finv.append(fi)
            self.inv.append(v)

    def __call__(self, n, r):
        if len(self.fac) <= n:
            self.prep(n)
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.mod

def main():
    H, W, A, B = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    nCr = nCrMod(mod)
    r = 0
    a = H - A - 1
    for i in range(B, W):
        r = (r + nCr(a + i, i) * nCr(A - 1 + W - i - 1, W - i - 1)) % mod
    return r


print((main()))

