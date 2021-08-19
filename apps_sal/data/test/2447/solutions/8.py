from math import *


def r1(t):
    return t(input().strip())


def r2(t):
    return [t(i) for i in input().strip().split()]


def r3(t):
    return [t(i) for i in input().strip()]


for _ in range(int(input())):
    t = r3(int)
    ps = 0
    ss = sum(t)
    n = len(t)
    ans = n
    for i in range(0, n):
        if i > 0:
            ss -= t[i - 1]
            ps += t[i - 1]
        res = min(i - ps + ss, ps + n - i - ss)
        ans = min(res, ans)
    print(ans)
