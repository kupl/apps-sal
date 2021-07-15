class ModInt:
    def __init__(self, num, mod):
        self.num = num
        self.mod = mod

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return "ModInt(num: {}, mod: {}".format(self.num, self.mod)

    def __add__(self, other):
        ret = self.num + other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __sub__(self, other):
        ret = self.num - other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __mul__(self, other):
        ret = self.num * other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def pow(self, times):
        pw = pow(self.num, times, self.mod)
        return ModInt(pw, self.mod)

    def inverse(self):
        return self.pow(self.mod - 2)

    def __truediv__(self, other):
        num = self * other.inverse()
        return ModInt(num, self.mod)


h, w, a, b = list(map(int, input().split()))
mod = 10 ** 9 + 7

fact = [ModInt(1, mod)]
inv = [ModInt(1, mod).inverse()] * (h + w - 1)


def comb(n, r):
    return fact[n] * inv[r] * inv[n-r]


for i in range(1, h + w - 1):
    fact.append(fact[-1] * ModInt(i, mod))

inv[h+w-2] = fact[-1].inverse()
for i in range(h + w - 2, 0, -1):
    inv[i-1] = inv[i] * ModInt(i, mod)

ans = ModInt(0, mod)
for hi in range(h - a):
    ans += comb(hi + b - 1, hi) * comb(h - hi - 1 + w - b - 1, w - b - 1)

print(ans)

