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
        n = I()
        l = list(In())
        ans = -1
        for x in range(1, n - 1):
            if l[x - 1] < l[x] and l[x] > l[x + 1]:
                ans = x
                break
        if ans == -1:
            no()
        else:
            yes()
            print(ans, ans + 1, ans + 2)

    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(I()):
        main()


__starting_point()
