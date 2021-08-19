from fractions import Fraction
import collections
MOD = 998244353


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        (g, y, x) = egcd(b % a, a)
        return (g, x - b // a * y, y)


def modinv(a, m):
    (g, x, y) = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


nkids = int(input())
cnts = collections.defaultdict(int)
pickprobs = collections.defaultdict(int)
for i in range(nkids):
    ls = list(map(int, input().split()))[1:]
    md = modinv(len(ls), MOD)
    for e in ls:
        cnts[e] += 1
        pickprobs[e] += md
res = 0
mdd = modinv(nkids ** 2, MOD)
for k in list(cnts.keys()):
    res += cnts[k] * pickprobs[k] * mdd
print(res % MOD)
