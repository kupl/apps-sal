import operator
import math
import itertools
import functools
mod = int(1000000000.0 + 7)


def factor(n):
    a = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            a.append(i)
            n //= i
    if n > 1:
        a.append(n)
    return a


def comp(n):
    f = set(factor(n))
    c = pow(2, n - 1, mod)
    for i in range(1, len(f) + 1):
        if i & 1:
            sign = -1
        else:
            sign = 1
        for j in itertools.combinations(f, i):
            k = functools.reduce(operator.mul, j)
            c += sign * pow(2, n // k - 1, mod)
            c = c % mod
    return c


(x, y) = map(int, input().split())
if y % x == 0:
    print(comp(y // x))
else:
    print(0)
