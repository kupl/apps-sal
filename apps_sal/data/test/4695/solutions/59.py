import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    x, y = LI()
    d = {1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 0, 9: 1, 10: 0, 11: 1, 12: 0}

    if d[x] == d[y]:
        print('Yes')
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
