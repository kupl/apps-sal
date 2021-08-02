import sys
from sys import stdin, stdout

mod = 998244353

#fileIO = open("a.inp", "r")

n, k = stdin.readline().split()  # fileIO.readline().split()
n, k = int(n), int(k)


def hpow(x, y):
    if(y == 0): return 1
    if(y == 1): return x % mod
    a = hpow(x, y >> 1)
    a = (a * a) % mod
    return (a * x) % mod if y & 1 else a


def rev(x):
    return hpow(x, mod - 2)


def max(x, y):
    return x if x >= y else y


revk = rev(k)


def cal(l, x, y):
    rr = 1
    if(not x and not y):
        rr = k * hpow(k - 1, l - 1) % mod
        return rr
    if(not y): x, y = y, x
    if(not x):
        rr = k
        for i in range(l - 1): rr = rr * (k - 1) % mod
        return rr * revk % mod * (k - 1) % mod

    if(x == y):
        f = [[k - 1, 0]]
        for i in range(1, l):
            f.append([(f[i - 1][1] * (k - 1) % mod + f[i - 1][0] * (k - 2) % mod) % mod, f[i - 1][0]])
        return f[l - 1][0]

    # final case -> x ... y

    f = [[k - 2, 0, 1]]
    for i in range(1, l):
        f.append([((f[i - 1][1] + f[i - 1][2]) * (k - 2) % mod + f[i - 1][0] * max(0, k - 3) % mod) % mod, (f[i - 1][2] + f[i - 1][0]) % mod, (f[i - 1][1] + f[i - 1][0]) % mod])

    return (f[l - 1][0] + f[l - 1][1]) % mod


a = [int(x) for x in stdin.readline().split()]

# fileIO.close()

m1, m2 = 0, 0

b = [0]
c = [0]

for i in range(n):
    if(i & 1): b.append(a[i])
    else: c.append(a[i])

m1 = len(b) - 1
m2 = len(c) - 1

res = 1

# process array b & c separately

#fileIO = open("a.out","w")

for i in range(1, m1 + 1):
    if(b[i] > 0 and b[i] == b[i - 1]):
        stdout.write(str(0))  # fileIO.write(str(0))
        return
for i in range(1, m2 + 1):
    if(c[i] > 0 and c[i] == c[i - 1]):
        stdout.write(str(0))
        return

j = -1
for i in range(1, m1 + 1):
    if(b[i] == -1):
        if(j < 0): j = i
        if(i >= m1 or b[i + 1] != -1):
            res = res * cal(i - j + 1, 0 if j <= 1 else b[j - 1], 0 if i >= m1 else b[i + 1]) % mod
            j = -1

j = -1
for i in range(1, m2 + 1):
    if(c[i] == -1):
        if(j < 0): j = i
        if(i >= m2 or c[i + 1] != -1):
            res = res * cal(i - j + 1, 0 if j <= 1 else c[j - 1], 0 if i >= m2 else c[i + 1]) % mod
            j = -1

stdout.write(str(res))
# fileIO.close()
