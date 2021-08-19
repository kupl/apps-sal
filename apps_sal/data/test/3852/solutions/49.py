import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def ValueToBits(x, digit):
    res = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        res[i] = now % 2
        now = now >> 1
    return res


def BitsToValue(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans += arr[i] * 2 ** i
    return ans


def ZipArray(a):
    aa = [[a[i], i] for i in range(n)]
    aa.sort(key=lambda x: x[0])
    for i in range(n):
        aa[i][0] = i + 1
    aa.sort(key=lambda x: x[1])
    b = [aa[i][0] for i in range(len(a))]
    return b


def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit - i - 1] = now % 10
        now = now // 10
    return ans


def Zeros(a, b):
    if b <= -1:
        return [0 for i in range(a)]
    else:
        return [[0 for i in range(b)] for i in range(a)]


def AddV2(v, w):
    return [v[0] + w[0], v[1] + w[1]]


dir4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def clamp(x, y, z):
    return max(y, min(z, x))


class Bit:

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def Zaatsu(a):
    a.sort()
    now = a[0][0]
    od = 0
    for i in range(n):
        if now == a[i][0]:
            a[i][0] = od
        else:
            now = a[i][0]
            od += 1
            a[i][0] = od
    a.sort(key=lambda x: x[1])
    return a


class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


'\ndef cmb(n, r, p):\n    if (r < 0) or (n < r):\n        return 0\n    r = min(r, n - r)\n    return fact[n] * factinv[r] * factinv[n-r] % p\n\np = 2\nN = 10 ** 6 + 2\nfact = [1, 1]  # fact[n] = (n! mod p)\nfactinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)\ninv = [0, 1]  # factinv 計算用\n\nfor i in range(2, N + 1):\n    fact.append((fact[-1] * i) % p)\n    inv.append((-inv[p % i] * (p // i)) % p)\n    factinv.append((factinv[-1] * inv[-1]) % p)\n\n'


def rl(x):
    return list(range(len(x)))


n = int(input())
a = list(map(int, input().split()))
if abs(max(a)) >= abs(min(a)):
    idx = -1
    mx = -1
    for i in range(n):
        if mx <= a[i]:
            idx = i + 1
            mx = a[i]
    print(n * 2)
    print((idx, n))
    print((idx, n))
    for i in range(n - 1):
        print((n, i + 1))
        print((n, n))
else:
    idx = -1
    mi = 1
    for i in range(n):
        if mi >= a[i]:
            idx = i + 1
            mi = a[i]
    print(n * 2)
    print((idx, 1))
    print((idx, 1))
    for i in range(n, 1, -1):
        print((1, i))
        print((1, 1))
