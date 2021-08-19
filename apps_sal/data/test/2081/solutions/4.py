import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def gt(a, b):
    return a > b


def gte(a, b):
    return a >= b


def lt(a, b):
    return a < b


def lte(a, b):
    return a <= b


def d(a, cmp, val):
    n = len(a)
    st = [(val, -1)]
    r = [0] * n
    for i in range(len(a)):
        v = a[i]
        while cmp(v, st[-1][0]):
            st.pop()
        r[i] = st[-1][1]
        st.append((v, i))
        # print(st)
    return r


def rr(a):
    n = len(a)
    r = [0] * n
    for i in range(n):
        r[n - i - 1] = n - a[i] - 1
    return r


n = mint()
a = list(mints())
b = a[::-1]
Ml = d(a, gt, (10**9))
Mr = rr(d(b, gte, (10**9)))
ml = d(a, lt, -(10**9))
mr = rr(d(b, lte, -(10**9)))
# print(a)
# print(Ml)
# print(Mr)
# print(b)
# print(ml)
# print(mr)
r = 0
for i in range(n):
    r += a[i] * ((i - Ml[i]) * (Mr[i] - i) - (i - ml[i]) * (mr[i] - i))
print(r)
