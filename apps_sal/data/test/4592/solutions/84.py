import collections
import numpy
n = int(input())
x = []


def factorization(n):
    d = []
    while n % 2 == 0:
        d.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            d.append(int(f))
            n /= f
        else:
            f += 2
    if n != 1:
        d.append(n)
    return d


for i in range(n, 1, -1):
    x += factorization(i)
c = collections.Counter(x)
l = list(c.values())
ans = 1
for i in range(len(l)):
    ans *= 1 + l[i]
print(ans % (7 + 10 ** 9))
