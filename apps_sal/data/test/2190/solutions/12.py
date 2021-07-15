import math


def fac(a):
    ans = {}

    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            ans[i] = 0
            while a % i == 0:
                a //= i
                ans[i] += 1

    ans[a] = 1

    return ans


def inverse(a, k):
    buf = {}

    for j in a.keys():
        buf[j] = (k - a[j] % k) % k

    return buf


def normal(a, k):
    buf = {}

    for j in a.keys():
        buf[j] = a[j] % k

    return buf


def getHash(d):
    ans = 1
    for i in d.keys():
        ans *= i ** d[i]
    return ans


n, k = map(int, input().split(' '))

a = [i for i in map(int, input().split(' '))]

b = [i for i in map(fac, a)]

factors = {}

for i in b:
    buf = getHash(inverse(i, k))
    if buf in factors.keys():
        factors[buf] += 1
    else:
        factors[buf] = 1

ans = 0

for i in range(len(b)):
    b[i] = normal(b[i], k)
    if getHash(b[i]) == getHash(inverse(b[i], k)):
        ans -= 1

for i in map(getHash, b):
    if i in factors.keys():
        ans += factors[i]

print(ans // 2)
