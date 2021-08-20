import numpy as np
dic = dict()
mod = 10 ** 9 + 7
p = 0


def reg(a, b):
    if a < 0 or (a == 0 and b < 0):
        (a, b) = (-a, -b)
    if b > 0:
        return (0, a, b)
    else:
        return (1, -b, a)


n = int(input())
for _ in range(n):
    (a, b) = map(int, input().split())
    if a == 0 and b == 0:
        p += 1
        continue
    ab = np.gcd(a, b)
    (a, b) = (a // ab, b // ab)
    (idx, a, b) = reg(a, b)
    k = (a, b)
    if k not in dic.keys():
        dic[k] = [0, 0]
    dic[k][idx] += 1
not_p = 1
for k in dic.keys():
    (a, b) = k
    (pp, pm) = dic[k]
    not_p *= (pow(2, pp, mod) + pow(2, pm, mod) - 1) % mod
    not_p %= mod
print((p + not_p - 1) % mod)
