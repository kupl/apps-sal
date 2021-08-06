a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


g = gcd(a, b)
f = factorize(g)
print(len(set(f)) + 1)
