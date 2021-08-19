import math


def getPrimes(v):
    d = 2
    gr = int(math.sqrt(v)) + 1
    res = []
    while d <= gr and v > 1:
        if v % d == 0:
            res.append(d)
            while v % d == 0:
                v //= d
        d += 1
    if v > 1:
        res.append(v)
    return res


def solve(p, y):
    x = y
    while x > p:
        pr = getPrimes(x)
        if all((v > p for v in pr)):
            return x
        x -= 1
    return -1


(p, y) = list(map(int, input().split()))
print(solve(p, y))
