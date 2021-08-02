n, k = map(int, input().split())
P = 10**9 + 7


class FactInv:
    def __init__(self, N, P):
        fact = []; ifact = []; fact = [1] * (N + 1); ifact = [0] * (N + 1)
        for i in range(1, N):
            fact[i + 1] = (fact[i] * (i + 1)) % P
        ifact[-1] = pow(fact[-1], P - 2, P)
        for i in range(N, 0, -1):
            ifact[i - 1] = (ifact[i] * i) % P
        self.fact = fact; self.ifact = ifact; self.P = P

    def comb(self, n, k):
        return (self.fact[n] * self.ifact[k] * self.ifact[n - k]) % self.P


C = FactInv(2 * n + 10, P)
ans = 0
for i in range(0, min(k + 1, n)):
    ans += (C.comb(n, i) * C.comb(n - 1, n - i - 1)) % P
    ans %= P
print(ans)
