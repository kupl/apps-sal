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
    n, m = LI()
    a = [LI() for _ in range(n)] + [[-1] * m]
    rr = list(range(n))
    for j in range(m):
        l = 0
        for r in range(1, n + 1):
            if a[r][j] < a[r - 1][j]:
                while l < r:
                    if rr[l] < r - 1:
                        rr[l] = r - 1
                    else:
                        l = r
                        break
                    l += 1

    k = II()
    ans = []
    for _ in range(k):
        l, r = LI()
        if rr[l - 1] >= r - 1:
            ans.append('Yes')
        else:
            ans.append('No')

    print('\n'.join(ans))


main()
