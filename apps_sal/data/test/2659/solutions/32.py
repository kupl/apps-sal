import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log10
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
K = INT()


def S(n):
    return sum([int(x) for x in list(n)])


def f(N):
    sunuke = []
    for d in range(-1, int(log10(N) + 1)):
        sunuke.append(10 ** (d + 1) * (N // 10 ** (d + 1) + 1) - 1)
    sunuke2 = [x / S(str(x)) for x in sunuke]
    return sunuke[sunuke2.index(min(sunuke2))]


N = 1
for _ in range(K):
    print(N)
    N = f(N + 1)
