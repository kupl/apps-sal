'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College
    Date:10/06/2020

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
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


def check(x):
    x1 = int(sqrt(x))
    return x1 * x1 == x


def solve():

    n = ii()
    a = li()
    tmp = [0] * n
    tot = 0
    x = 1
    for i in range(n // 2):
        tmp[2 * i + 1] = a[i]
        while(x < 1000000):
            if x * x > tot and check(x * x + a[i]):
                tmp[2 * i] = x * x - tot
                break
            x += 1
        if(x == 1000000):
            print('No')
            return
        tot += tmp[2 * i] + a[i]
    print('Yes')
    print(*tmp)


def __starting_point():
    solve()


__starting_point()
