from math import ceil, floor, comb, factorial, gcd, pow, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(MAP())


n = INT()
s = input()
count = 0
for i in range(n):
    if s[i] == '(':
        count += 1
    else:
        count = max(0, count - 1)
s += ')' * count
count = 0
for i in range(n - 1, -1, -1):
    if s[i] == ')':
        count += 1
    else:
        count = max(0, count - 1)
s = '(' * count + s
print(s)
