'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush, heappop
from functools import cmp_to_key as ctk
from collections import deque, defaultdict as dd
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
from math import ceil, sqrt, log, gcd
def ii(): return int(input())
def si(): return input().rstrip()
def mi(): return map(int, input().split())
def li(): return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


file = 1


def solve():

    n, m = mi()
    a = li()
    b = li()
    a.sort()
    b.sort()
    if b[-1] <= a[0]:
        print(0)
        return
    pre = [0] * n
    for i in range(1, n):
        pre[i] += pre[i - 1]
        pre[i] += i * (a[i] - a[i - 1])

    suff = [0] * m
    for i in range(m - 2, -1, -1):
        suff[i] += suff[i + 1]
        suff[i] += (m - i - 1) * (b[i + 1] - b[i])

    def fun(m1):
        x = bisect(a, m1) - 1
        y = bisect(b, m1) - 1
        ans = 0
        if x == n:
            x -= 1
        ans += pre[x]
        ans += (m1 - a[x]) * (x + 1)
        if y >= (m - 1):
            return ans
        if y == 0:
            y -= 1
        ans += (b[y + 1] - m1) * (m - y - 1)
        ans += suff[y + 1]
        return ans

    l = 1
    r = int(1e9 + 5)
    while(l <= r):
        mid = l + (r - l) // 2
        x = fun(mid)
        if mid == 1:
            x1 = fun(mid + 1)
            if(x > x1):
                l = mid + 1
                ans = x1
            else:
                print(max(x, 0))
                return

        x1 = fun(mid - 1)
        x2 = fun(mid + 1)
        if(x1 < x2):
            if(x1 < x):
                r = mid - 1
                ans = x1
            else:
                print(max(x, 0))
                return
        else:
            if(x2 < x):
                l = mid + 1
            else:
                print(max(x, 0))
                return


def __starting_point():

    if(file):

        if path.exists('input.txt'):
            sys.stdin = open('input.txt', 'r')
            sys.stdout = open('output.txt', 'w')
        else:
            input = sys.stdin.readline
    solve()


__starting_point()
