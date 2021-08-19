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


def ips():
    return input().split()


ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF = 10 ** 15


def ceilab(a, b):
    return (a + b - 1) // b


(a, b, x, y) = ma()
if y > 2 * x:
    y = 2 * x
if a == b:
    print(x)
elif a > b:
    print((a - b - 1) * y + x)
else:
    print((b - a) * y + x)
