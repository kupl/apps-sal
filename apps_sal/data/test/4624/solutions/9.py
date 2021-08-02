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
# mod=1000000007
mod = 998244353
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


def solve():

    for _ in range(ii()):

        n, x = mi()
        if n <= 2:
            print(1)
            continue

        c = 2
        p = 2 + x
        while(n > p):
            p += x
            c += 1
        print(c)


def __starting_point():

    if path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    else:
        input = sys.stdin.readline
    solve()


__starting_point()
