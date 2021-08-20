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


s = input()
tmp = 10 ** 11
for i in range(0, len(s) - 2):
    tmp = min(tmp, abs(753 - int(s[i:i + 3])))
print(tmp)
