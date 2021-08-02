import math
import sys
import itertools

A = 'A'
B = 'B'


def c(s):
    caa, cab, cba, cbb = s
    return {A: {A: caa, B: cab}, B: {A: cba, B: cbb}}


def f(s, n, C):
    if len(s) == n:
        yield s
    else:
        for i in range(len(s) - 1):
            yield from f(s[:i + 1] + C[s[i]][s[i + 1]] + s[i + 1:], n, C)


def g(n, s):
    return len(set(f('AB', n, c(s))))


n = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
s = ''.join([caa, cab, cba, cbb])
mod = 10**9 + 7

X = g(6, s)
if n == 2:
    print(1)
elif X == 8:
    print(pow(2, n - 3, mod))
elif X == 5:
    a = 0
    b = 1
    for i in range(n - 2):
        a, b = b, (a + b) % mod
    print(b)
elif X == 1:
    print(1)

for sx in itertools.product(*[[A, B]] * 4):
    s = ''.join(sx)
    print(' '.join([s, *['%2d' % g(i, s) for i in range(2, 10)]]), file=sys.stderr)
