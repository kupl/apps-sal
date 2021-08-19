N = int(input())
S = input()
dic = {}
for (i, s) in enumerate(S):
    if s in dic:
        dic[s].append(i)
    else:
        dic[s] = [i]
X = list(range(N - 1, -1, -1))
for (c, idcs) in list(dic.items()):
    for (p, q) in zip(idcs, reversed(idcs)):
        X[p] = N - 1 - q


class BIT:

    def __init__(self, N):
        self.N = N
        self.T = [0] * (N + 1)

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.T[i] += x
            i += i & -i

    def _sum(self, i):
        ret = 0
        while i > 0:
            ret += self.T[i]
            i ^= i & -i
        return ret

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = 1 << self.N.bit_length()
        while k:
            if x + k <= self.N and self.T[x + k] < w:
                w -= self.t[x + k]
                x += k
                k >>= 1
        return x + 1


b = BIT(N)
ans = 0
for (i, x) in enumerate(X):
    ans += i - b._sum(x + 1)
    b.add(x, 1)
print(ans)
