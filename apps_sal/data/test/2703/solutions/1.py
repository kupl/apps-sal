from sys import stdin, stdout
import math
import sys
import heapq
from itertools import permutations, combinations
from collections import defaultdict, deque, OrderedDict
from os import path
import random
import bisect as bi
def yes(): print('YES')
def no(): print('NO')


if (path.exists('input.txt')):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    def I(): return (int(input()))
    def In(): return(map(int, input().split()))
else:
    def I(): return (int(stdin.readline()))
    def In(): return(map(int, stdin.readline().split()))


def dict(a):
    d = {}
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1
        else:
            d[x] = 1
    return d


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bi.bisect_right(a, x)
    if i != len(a):
        return i
    else:
        return -1


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return -1


def main():
    try:
        n, Q = In()
        l = list(In())
        l.sort()
        pre = [0]
        su = 0
        for x in range(n):
            su += l[x]
            pre.append(su)
        for x in range(Q):
            q = I()
            q *= 2
            pos = find_ge(l, q)
            if pos == -1:
                print(0)
            else:
                ans = pre[-1] - pre[pos]
                print(ans)
    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(1):
        main()


__starting_point()
