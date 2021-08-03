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


def RLE(s):
    res = []
    prev = ""
    cnt = 0
    for e in s:
        if prev == "":
            prev = e
            cnt += 1
        elif prev == e:
            cnt += 1
        else:
            res.append((cnt, prev))
            prev = e
            cnt = 1
    res.append((cnt, prev))
    return res


def __starting_point():
    s = input()
    rle = RLE(s)
    # print(rle)
    print(len(rle) - 1)


__starting_point()
