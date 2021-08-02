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
    n = II()
    l = list(range(1, n + 1))
    l = l[:][::-1]
    print(*l)
