import math
a, b = map(int, input().split())


def factorize(x):
    i = 2
    res = []
    while i * i <= x:
        while x % i == 0:
            x //= i
            res.append(i)
        i += 1
    if x > 1:
        res.append(x)
    return res


g = math.gcd(a, b)
f = factorize(g)
print(len(set(f)) + 1)
