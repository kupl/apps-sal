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
    a, b, x, y, n = MI()
    if a - min(n, a - x) < b - min(n, b - y):
        b, a = a, b
        y, x = x, y
    temp = min(n, b - y)
    n -= temp
    b -= temp
    a -= min(a - x, n)
    print(a * b)
