from sys import stdin, stdout
import math
import sys
from itertools import permutations, combinations
from collections import defaultdict, deque, OrderedDict
from os import path
import bisect as bi
import heapq
def yes(): print('YES')
def no(): print('NO')


if (path.exists('input.txt')):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    def I(): return (int(input()))
    def In(): return(list(map(int, input().split())))
else:
    def I(): return (int(stdin.readline()))
    def In(): return(list(map(int, stdin.readline().split())))


def dict(a):
    d = {}
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1
        else:
            d[x] = 1
    return d


def main():
    try:
        n, X = In()
        l = list(In())
        l.sort(reverse=True)
        mi = -1
        j, ans = 0, 0
        for x in range(n):
            if mi == -1:
                mi = l[x]
                j = 1
            else:
                mi = min(mi, l[x])
                j += 1
            if mi * j >= X:
                ans += 1
                mi = -1
                j = 0
        print(ans)

    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(I()):
        main()


__starting_point()
