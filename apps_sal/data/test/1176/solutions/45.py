import bisect
import collections
import copy
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n = I()
    a = LI()
    ans = 0
    mn = 0
    for i in range(n):
        if a[i] < 0:
            mn += 1
            a[i] *= -1
    if mn % 2 == 0:
        ans = sum(a)
    else:
        ans = sum(a) - min(a) * 2
    print(ans)


main()
