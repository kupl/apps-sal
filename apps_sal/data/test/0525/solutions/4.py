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
    print(1 if len(set(a)) != 1 else n)
