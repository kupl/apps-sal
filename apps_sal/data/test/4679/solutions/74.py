import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
S = [deque(input().replace('a', '0').replace('b', '1').replace('c', '2')) for _ in range(3)]
next = '0'
while True:
    tmp = S[int(next)]
    if len(tmp) == 0:
        ans = next
        break
    else:
        next = tmp.popleft()
if ans == '0':
    print('A')
elif ans == '1':
    print('B')
else:
    print('C')
