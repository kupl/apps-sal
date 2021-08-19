from math import *
(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
ma = max(a)
p = []
prime = [True] * (ma + 1)
prime[0] = False
prime[1] = False
for i in range(2, ma + 1):
    if prime[i]:
        p.append(i)
        if i ** 2 <= n:
            for j in range(i ** 2, ma + 1, i):
                prime[j] = False


def factor(x):
    res = {}
    sq = ceil(sqrt(x))
    for i in p:
        if i > sq or x <= 1:
            break
        if x % i == 0:
            res[i] = 0
            while x % i == 0:
                res[i] += 1
                x //= i
    if x > 1:
        res[x] = 1
    nres = []
    for j in res:
        if res[j] % k > 0:
            nres.append((j, res[j] % k))
    return tuple(nres)


d = {}
for i in range(n):
    f = factor(a[i])
    if f not in d:
        d[f] = 1
    else:
        d[f] += 1
ans = 0
for x in d:
    y = []
    for i in x:
        y.append((i[0], k - i[1]))
    y = tuple(y)
    if y in d:
        if y != x:
            ans += d[x] * d[y]
        else:
            ans += d[x] * (d[y] - 1)
print(ans // 2)
