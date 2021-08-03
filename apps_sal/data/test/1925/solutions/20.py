import bisect
import collections
import copy
import itertools
import math
import string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    a, b, n = LI()
    ans = 0

    def f(a, b, x):
        ans = (a * x) // b - a * (x // b)
        return ans
    if b - 1 <= n:
        ans = f(a, b, b - 1)
    else:
        ans = f(a, b, n)
    print(ans)


main()
