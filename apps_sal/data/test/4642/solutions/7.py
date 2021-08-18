import sys
from collections import defaultdict as dd
from collections import deque
from functools import *
from fractions import Fraction as f
from copy import *
from bisect import *
from heapq import *
from math import *
from itertools import permutations, product


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1

if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')


def inc(d, c):
    d[c] = d[c] + 1 if c in d else 1


def bo(i):
    return ord(i) - ord('A')


def li():
    return [int(xx) for xx in input().split()]


def fli():
    return [float(x) for x in input().split()]


def comp(a, b):
    if(a > b):
        return 2
    return 2 if a == b else 0


def gi():
    return [xx for xx in input().split()]


def fi():
    return int(input())


def pro(a):
    return reduce(lambda a, b: a * b, a)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def si():
    return list(input().rstrip())


def mi():
    return map(int, input().split())


def gh():
    sys.stdout.flush()


def isvalid(i, j):
    return 0 <= i < n and 0 <= j < n


def bo(i):
    return ord(i) - ord('a')


def graph(n, m):
    for i in range(m):
        x, y = mi()
        a[x].append(y)
        a[y].append(x)


t = fi()

while t > 0:
    t -= 1
    n, x, y = mi()
    p = n - 2
    x, y = max(x, y), min(x, y)
    for i in range(1, p + 2):
        if (x - y) % i == 0:
            ans = i
    p = (x - y) // ans
    for i in range(n):
        if x - i * p <= 0:
            break
        mini = x - i * p
    for i in range(n):
        print(mini + p * i, end=" ")
    print()
