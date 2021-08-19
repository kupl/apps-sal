from math import floor, ceil, pi
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, accumulate, groupby, product
from collections import defaultdict
from collections import Counter, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def LI2():
    return [int(input()) for i in range(n)]


def MXI():
    return [[LI()] for i in range(n)]


def SI():
    return input().rstrip()


def printns(x):
    print('\n'.join(x))


def printni(x):
    print('\n'.join(list(map(str, x))))


inf = 10 ** 17
mod = 10 ** 9 + 7
s = SI()
k = I()
n = len(s)
strs = []
for i in range(n):
    for j in range(1, k + 1):
        strs.append(s[i:i + j])
print(sorted(list(set(strs)))[k - 1])
