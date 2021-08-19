import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


try:
    import numpy

    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
    dprint('debug mode')
except Exception:

    def dprint(*args, **kwargs):
        pass


def e_gcd(a, b):
    if a == 0 and b == 0:
        return (-1, 0, 0)
    if b == 0:
        return (a, 1, 0)
    (d, y, x) = e_gcd(b, a % b)
    y -= a // b * x
    return (d, x, y)


def m_reverse(a, n):
    (d, x, y) = e_gcd(a, n)
    dprint(x, y, a, n)
    assert x * a + y * n == d
    if d == 1:
        if x % n <= 0:
            return x % n + n
        else:
            return x % n
    else:
        return -1


inId = 0
outId = 0
if inId > 0:
    dprint('use input', inId)
    sys.stdin = open('input' + str(inId) + '.txt', 'r')
if outId > 0:
    dprint('use output', outId)
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')
    atexit.register(lambda: sys.stdout.close())
base = 998244353
d = 1233
t = m_reverse(d, base)
dprint(t)
z = t * d % base
dprint(z)
(N, M, K) = getIntList()
J = N - 1 - K
Z = N - J
dprint(Z)
R = M
for i in range(Z - 1):
    R *= M - 1
    R %= base
dprint(R)
n0 = J
m0 = Z
dprint(n0, m0)
for i in range(m0 - 1):
    g = n0 + m0 - 1 - i
    R *= g
    R %= base
for i in range(2, m0):
    t = m_reverse(i, base)
    R *= t
    R %= base
print(R)
