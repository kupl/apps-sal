'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from functools import cmp_to_key as ctk
from collections import deque, defaultdict as dd
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
from math import ceil, sqrt, log, gcd
def ii(): return int(input())
def si(): return input()
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod = 1000000007
# mod=998244353
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


def solve():

    n, m, w = mi()
    a = li()

    def fessible(mid):

        b = [0] * (n + 1)
        moves = 0
        for i in range(1, n + 1):
            b[i] += b[i - 1]
            x = a[i - 1] + b[i]

            if(x < mid):
                b[i] += (mid - x)
                if(i + w <= n):
                    b[i + w] -= (mid - x)
                moves += (mid - x)

        return moves <= m

    l = 1
    r = 1e10
    while(l <= r):
        mid = l + (r - l) // 2
        if(fessible(mid)):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(int(ans))


def __starting_point():
    solve()


__starting_point()
