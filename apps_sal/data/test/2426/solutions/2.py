from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 10 ** 9 + 7


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n').split(' ')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    n = val()
    a = li()
    if len(a) == 1 and a[0] & 1:
        print(-1)
        continue
    if not a[0] & 1:
        print(1)
        print(1)
    elif not a[1] & 1:
        print(1)
        print(2)
    else:
        print(2)
        print('1 2')
