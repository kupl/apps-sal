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
    n, x = MI()
    a = sorted(LI())
    a = a[::-1]
    l = 0
    count = 1
    ans = 0
    while l < n:
        if count * a[l] >= x:
            ans += 1
            count = 1
        else:
            count += 1
        l += 1
    print(ans)
