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


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return -1


def main():
    try:
        n = I()
        l = list(In())
        z = set()
        flag = 0
        for x in l:
            if x not in z:
                z.add(x)
            else:
                flag = 1
                break
        if flag:
            yes()
        else:
            no()
    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(I()):
        main()


__starting_point()
