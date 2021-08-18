# ----------------
# ここから
# ----------------

import sys
from io import StringIO
import unittest
import collections


def yn(b):
    print(("Yes" if b == 1 else "No"))
    return


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def resolve():
    readline = sys.stdin.readline
    a, b = list(map(int, readline().rstrip().split()))

    af = factorization(a)
    bf = factorization(b)

    c = collections.Counter()
    c[1] = 2
    for x in af:
        c[x[0]] += 1
    for x in bf:
        c[x[0]] += 1
    ans = 0
    for k in list(c.keys()):
        if c[k] >= 2:
            ans += 1
    print(ans)

    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
