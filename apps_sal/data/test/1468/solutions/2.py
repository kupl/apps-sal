import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7


def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n = II()
    a = [S() for _ in range(n)]
    for i in range(n - 2, -1, -1):
        t = a[i]
        s = a[i + 1]
        sl = len(s)
        for j in range(1, len(t)):
            if j >= sl:
                a[i] = s
                break
            if t[j] > s[j]:
                a[i] = t[:j]
                break
            if t[j] < s[j]:
                break

    print('\n'.join(a))


main()
