N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

mod = 10**9 + 7


class Combination:
    def __init__(self, n):
        self.facts = [1 for i in range(n + 1)]
        self.invs = [1 for i in range(n + 1)]

        for i in range(1, n + 1):
            self.facts[i] = self.facts[i - 1] * i % mod
        self.invs[n] = pow(self.facts[n], mod - 2, mod)
        for i in range(1, n + 1):
            self.invs[n - i] = self.invs[n - i + 1] * (n - i + 1) % mod

    def ncr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.facts[n] * self.invs[r] * self.invs[n - r] % mod

    def nhr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.ncr(n + r - 1, n - 1)


comb = Combination(N)

if K == 1:
    print(0)
    return

ans = 0
for i in range(N - K + 1):
    ans += (comb.ncr(N - 1 - i, K - 1) * A[i] - comb.ncr(N - 1 - i, K - 1) * A[N - 1 - i]) % mod

print(ans % mod)
