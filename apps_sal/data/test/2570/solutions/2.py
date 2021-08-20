import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return map(int, sys.stdin.readline().split())


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    (n, x) = MI()
    a = LI()
    b = LI()
    a.sort()
    boo = True
    b.sort(reverse=True)
    for i in range(n):
        if a[i] + b[i] > x:
            boo = False
            break
    print('Yes' if boo else 'No')
    if q != t - 1:
        a = input()
