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
    return print('Yes') if fl else print('No')


n = ni()
cnts = []
for i in range(n):
    cnts.append(collections.Counter(list(input())))
ans = ''
alp = list('abcdefghijklmnopqrstuvwxyz')
for w in alp:
    tmp = 10 ** 10
    for i in range(n):
        tmp = min(tmp, cnts[i][w])
    ans += w * tmp
print(ans)
