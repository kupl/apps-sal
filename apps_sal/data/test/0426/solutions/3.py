# -*- coding: utf-8 -*-
import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); return
# template


def main():
    n, k = mi()
    s = li()
    if k == 0:
        print(''.join(s))
        return
    if n == 1:
        print(0)
        return
    cnt = 0
    if s[0] != "1":
        s[0] = "1"
        cnt += 1
    i = 1
    while cnt < k:
        if i > n - 1:
            break
        else:
            if s[i] != "0":
                s[i] = "0"
                cnt += 1
        i += 1
    print(''.join(s))
    return


def __starting_point():
    main()


__starting_point()
