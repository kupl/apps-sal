import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits


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
MOD = 10 ** 9 + 7
N = INT()
TA = [LIST() for _ in range(N)]
vote_T = 1
vote_A = 1
for (x, y) in TA:
    n = max(-(-vote_T // x), -(-vote_A // y))
    vote_T = x * n
    vote_A = y * n
print(vote_A + vote_T)
