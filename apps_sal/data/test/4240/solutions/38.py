from itertools import groupby


class Combination:

    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1 for i in range(self.n + 1)]
        self.finv = [1 for i in range(self.n + 1)]
        for i in range(2, self.n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.finv[i] = self.finv[i - 1] * pow(i, -1, self.mod) % self.mod

    def comb(self, n, m):
        return self.fac[n] * (self.finv[n - m] * self.finv[m] % self.mod) % self.mod


def iparse():
    return list(map(int, input().split()))


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for (k, v) in grouped:
        res.append((k, str(len(list(v)))))
    return res


def __starting_point():
    s = input()
    t = input()
    s = s + s
    for i in range(len(t)):
        if t == s[i:i + len(t)]:
            print('Yes')
            return
    print('No')


__starting_point()
