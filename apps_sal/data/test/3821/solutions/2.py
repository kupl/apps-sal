import fractions
import operator
import functools


def calc(d, nd, n):

    r = 0
    for i in range(n):

        r += d[i] * functools.reduce(operator.mul, nd[:i] + nd[i + 1:n], 1)

    return r


n = int(input())
# x = tuple(sorted(map(fractions.Fraction, str.split(input())), reverse=True))
x = tuple(sorted(map(float, str.split(input())), reverse=True))
nx = tuple([1 - p for p in x])

p = 0
for i in range(1, n + 1):

    p = max(p, calc(x[:i], nx[:i], i))

print(float(p))

