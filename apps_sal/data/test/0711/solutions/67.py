MOD = 10 ** 9 + 7
(N, M) = list(map(int, input().split()))


def factoring(k):
    import math
    dic = dict()
    n = int(math.sqrt(k)) + 2
    for i in range(2, n):
        count = 0
        while k % i == 0:
            count += 1
            k = k // i
        if count != 0:
            dic[i] = count
    if k != 1:
        dic[k] = 1
    return dic


class Factorial:

    def __init__(self, n, mod):
        self.f = [1]
        self.mod = mod
        for j in range(1, n + 1):
            self.f.append(self.f[-1] * j % mod)
        self.i = [pow(self.f[-1], mod - 2, mod)]
        for j in range(n, 0, -1):
            self.i.append(self.i[-1] * j % mod)
        self.i.reverse()

    def factorial(self, j):
        return self.f[j]

    def ifactorial(self, j):
        return self.i[j]

    def comb(self, n, k):
        return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod if n >= k else 0


C = Factorial(N + 100, MOD).comb
ans = 1
dic = factoring(M)
for tmp in dic:
    ans *= C(dic[tmp] + N - 1, dic[tmp])
    ans %= MOD
print(ans)
