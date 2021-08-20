from scipy.spatial.distance import euclidean, cityblock
import numpy as np
import re
import sys
import math
import itertools
import bisect
import heapq
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools


def v():
    return input()


def k():
    return int(input())


def S():
    return input().split()


def I():
    return list(map(int, input().split()))


def X():
    return list(input())


def L():
    return list(input().split())


def l():
    return list(map(int, input().split()))


def lcm(a, b):
    return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 6)
mod = 10 ** 9 + 7
cnt = 0
ans = 0
num = []
inf = float('inf')
al = 'abcdefghijklmnopqrstuvwxyz'
AL = al.upper()
n = k()
p = 0
a = []
b = []
for i in range(n):
    (A, B) = I()
    a.append(A)
    b.append(B)
z = []
w = []
for i in range(n):
    z.append(a[i] + b[i])
    w.append(a[i] - b[i])
print(max(max(z) - min(z), max(w) - min(w)))
