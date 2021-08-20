(n, m, k) = list(map(int, input().split()))
mod = 10 ** 9 + 7
MAX = n * m


class ModInt:

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return 'ModInt(num: {}, mod: {}'.format(self.num, mod)

    def __add__(self, other):
        ret = self.num + other.num
        ret %= mod
        return ModInt(ret)

    def __sub__(self, other):
        ret = self.num - other.num
        ret %= mod
        return ModInt(ret)

    def __mul__(self, other):
        ret = self.num * other.num
        ret %= mod
        return ModInt(ret)

    def pow(self, times):
        pw = pow(self.num, times, mod)
        return ModInt(pw)

    def inverse(self):
        return ModInt(inv[self.num])

    def __truediv__(self, other):
        num = self * other.inverse()
        return ModInt(num)


def comb(n, k):
    return fact[n] * inv[n - k] * inv[k]


fact = [None] * (MAX + 1)
fact[0] = ModInt(1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * ModInt(i)
inv = [None] * (MAX + 1)
inv[MAX] = fact[MAX].pow(mod - 2)
for i in range(MAX, 0, -1):
    inv[i - 1] = inv[i] * ModInt(i)
ans = ModInt(0)
for i in range(n):
    for j in range(m):
        add = ModInt(n - i) * ModInt(m - j) * ModInt(i + j)
        if i != 0 and j != 0:
            add *= ModInt(2)
        ans += add
ans *= comb(n * m - 2, k - 2)
print(ans)
