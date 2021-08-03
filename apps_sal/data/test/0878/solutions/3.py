from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import *
from itertools import *
import functools
import sys
from math import *
from decimal import *
from copy import *
getcontext().prec = 30
MAX = sys.maxsize
MAXN = 10**5 + 10
MOD = 10**9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN(x=" "):
    return(map(int, sys.stdin.readline().strip().split(x)))


def charIN(x=' '):
    return(sys.stdin.readline().strip().split(x))


def arrIN():
    return list(numIN())


def dis(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b)**0.5


def lgcd(a):
    g = a[0]
    for i in range(1, len(a)):
        g = math.gcd(g, a[i])
    return g


def ms(a):
    msf = -MAX
    meh = 0
    st = en = be = 0
    for i in range(len(a)):
        meh += a[i]
        if msf < meh:
            msf = meh
            st = be
            en = i
        if meh < 0:
            meh = 0
            be = i + 1
    return msf, st, en


def res(ans, t):
    print('Case #{}: {} {}'.format(t, ans[0], ans[1]))


n = int(input())
s = ''.join([str(i) for i in arrIN()])
ans = 0
for i in range(1, n):
    if s[i - 1] == '1':
        if s[i] == '2':
            ans += 3
        elif s[i] == '3':
            ans += 4
        else:
            print('Infinite')
            return
    elif s[i - 1] == '2':
        if s[i] == '2' or s[i] == '3':
            print('Infinite')
            return
        else:
            ans += 3
    else:
        if s[i] == '2' or s[i] == '3':
            print('Infinite')
            return
        else:
            ans += 4

ans -= s.count('312')
print('Finite')
print(ans)
