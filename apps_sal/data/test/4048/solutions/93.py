import math

n = int(input())


def p(x):
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def check(x):
    res = 10 ** 12
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            s = (i - 1) + (x // i - 1)
            res = min(res, s)
    return res


if p(n):
    print((n - 1))
else:
    print((check(n)))
