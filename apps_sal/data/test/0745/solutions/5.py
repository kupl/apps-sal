class Combination:
    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def C(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def P(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[n - r] % self.mod

    def H(self, n, r):
        if (n == 0 and r > 0) or r < 0:
            return 0
        return self.fac[n + r - 1] * self.facinv[r] % self.mod * self.facinv[n - 1] % self.mod

    def rising_factorial(self, n, r):
        return self.fac[n + r - 1] * self.facinv[n - 1] % self.mod

    def stirling_first(self, n, k):
        if n == k:
            return 1
        if k == 0:
            return 0
        return (self.stirling_first(n - 1, k - 1) + (n - 1) * self.stirling_first(n - 1, k)) % self.mod

    def stirling_second(self, n, k):
        if n == k:
            return 1
        return self.facinv[k] * sum((-1)**(k - m) * self.C(k, m) * pow(m, n, self.mod) for m in range(1, k + 1)) % self.mod

    def balls_and_boxes_3(self, n, k):
        return sum((-1)**(k - m) * self.C(k, m) * pow(m, n, self.mod) for m in range(1, k + 1)) % self.mod

    def bernoulli(self, n):
        if n == 0:
            return 1
        if n % 2 and n >= 3:
            return 0
        return (- pow(n + 1, self.mod - 2, self.mod) * sum(self.C(n + 1, k) * self.bernoulli(k) % self.mod for k in range(n))) % self.mod

    def faulhaber(self, k, n):
        return pow(k + 1, self.mod - 2, self.mod) * sum(self.C(k + 1, j) * self.bernoulli(j) % self.mod * pow(n, k - j + 1, self.mod) % self.mod for j in range(k + 1)) % self.mod

    def lah(self, n, k):
        return self.C(n - 1, k - 1) * self.fac[n] % self.mod * self.facinv[k] % self.mod

    def bell(self, n, k):
        return sum(self.stirling_second(n, j) for j in range(1, k + 1)) % self.mod


N, K = list(map(int, input().split()))
mod = 998244353
if K == 0:
    ans = 1
    for i in range(1, N + 1):
        ans = ans * i % mod
    print(ans)
    return
if K >= N:
    print(0)
    return

comb = Combination(200002, mod=mod)

print(comb.balls_and_boxes_3(N, N - K) * comb(N, K) * 2 % mod)
