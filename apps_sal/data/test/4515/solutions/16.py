from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


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
    (a, b, c, n) = li()
    (a, b, c) = sorted([a, b, c])
    if c - a > n:
        print('NO')
        continue
    else:
        n -= c - a
        a = c
    if c - b > n:
        print('NO')
        continue
    else:
        n -= c - b
        b = c
    if n % 3:
        print('NO')
        continue
    print('YES')
