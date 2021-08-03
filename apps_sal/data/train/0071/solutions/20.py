import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return list(map(int, sys.stdin.readline().split()))


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    n = II()
    a = LI()
    d = [0] * n
    s = 0
    for i in range(n):
        s += a[i]
        d[i] = s
    ans = min(d)
    if ans > 0:
        ans = 0
    print(-ans)
