class Combination:
    def __init__(self, mod, max_num):
        self.mod = mod
        self.fac = [0] * max_num
        self.finv = [0] * max_num
        self.inv = [0] * max_num

        self.fac[0], self.fac[1] = 1, 1
        self.finv[0], self.finv[1] = 1, 1
        self.inv[1] = 1

        for i in range(2, max_num):
            self.fac[i] = self.fac[i-1] * i % mod
            self.inv[i] = mod - self.inv[mod % i] * (mod // i) % mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % mod

    def calc(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * (
            self.finv[k] * self.finv[n - k] % self.mod) % self.mod


n, k = list(map(int, input().split()))
com = Combination(1000000007, 500000)

ret = 1

min_val = min(n, k)

for i in range(1, min_val+1):
    if i != n:
        ret += com.calc(n, i) * com.calc(n-1, i)
        ret %= 10 ** 9 + 7
    else:
        ret += 0

print(ret)

