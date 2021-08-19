from functools import reduce
from fractions import gcd
from collections import defaultdict, Counter
import copy
n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
dic = defaultdict(int)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


for i in a:
    c = Counter(prime_factorize(i))
    for (j, k) in c.items():
        if dic[j] < k:
            dic[j] = k
l = 1
for (i, j) in dic.items():
    l *= pow(i, j, mod)
point = 0
for i in a:
    point += l * pow(i, mod - 2, mod)
    point %= mod
print(point % mod)
