import sys
import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('YES') if fl else print('NO')


x = ni()
f = False
if x in [3, 5, 7]:
    f = True
yn(f)
