import collections


def logpow(a, b, mod):
    if b == 0:
        return 1

    v = logpow(a, b // 2, mod)
    ret = v * v % mod
    if b % 2 == 1:
        ret = ret * a % mod
    return ret


mod = 1000000007
n = int(input())

d = collections.defaultdict(int)
for x in input().split():
    d[int(x)] += 1

b = [(x, y) for x, y in list(d.items())]

pl = [1 for i in range(len(b) + 2)]
pr = [1 for i in range(len(b) + 2)]
for i in range(1, len(b) + 1):
    pl[i] = pl[i - 1] * (1 + b[i - 1][1]) % (mod - 1)
    j = len(b) - i + 1
    pr[j] = pr[j + 1] * (1 + b[j - 1][1]) % (mod - 1)


ret = 1
for i in range(1, len(b) + 1):
    pp = pl[i - 1] * pr[i + 1] % (mod - 1)
    pp = pp * (b[i - 1][1] * (b[i - 1][1] + 1) // 2) % (mod - 1)
    ret = ret * logpow(b[i - 1][0], pp, mod) % mod

print(ret)
