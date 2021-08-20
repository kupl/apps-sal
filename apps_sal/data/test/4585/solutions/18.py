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
    return print('Yes') if fl else print('No')


x = ni()
tmp = 0
for i in range(1, 10 ** 9):
    tmp += i
    if tmp >= x:
        break
print(i)
