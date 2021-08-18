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
MAXN = 10**6 + 10
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
    print('Case


def divi(n):
    l=[]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(n // i)
    return l


n=int(input())
a=arrIN()
b=arrIN()
c=[0] * n
b.sort()
for i in range(n):
    a[i] *= ((i + 1) * (n - i))

l=[[i, a[i]] for i in range(n)]
l.sort(key=lambda x: x[1], reverse=True)
j=0
for i in l:
    c[i[0]]=b[j]
    j += 1
ans=0
for i in range(n):
    ans += ((a[i] * c[i]) % 998244353)

print(ans % 998244353)
