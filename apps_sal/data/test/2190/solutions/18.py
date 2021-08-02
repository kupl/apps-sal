from collections import defaultdict


class Primes():
    def __init__(self, N):
        self.N = N
        self.prime = {i for i in range(2, self.N + 1)}
        self.spf = [-1] * (N + 1)
        for i in range(2, self.N + 1):
            if i in self.prime:
                self.spf[i] = i
                for j in range(i * 2, self.N + 1, i):
                    if j in self.prime:
                        self.spf[j] = i
                        self.prime.remove(j)

    def fact(self, Number):
        v = Number
        d = defaultdict(int)
        while v > 1:
            x = self.spf[v]
            d[x] += 1
            v //= x
        return d


P = Primes(10**5)

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = [0] * (10**5 + 1)
for v in a:
    cnt[v] += 1

ans = 0
for v in a:
    cnt[v] -= 1
    d = P.fact(v)
    res = 1
    for num, order in list(d.items()):
        res *= pow(num, (k - order % k) % k)
    if res <= 10**5:
        for i in range(1, 1000):
            if pow(i, k) * res > 10**5:
                break
            ans += cnt[pow(i, k) * res]
print(ans)
