from math import *
from collections import *
from random import *
from decimal import Decimal
from heapq import *
from bisect import *
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def lis():
    return list(map(int, input().split()))


def ma():
    return list(map(int, input().split()))


def inp():
    return int(input())


def st1():
    return input().rstrip('\n')


t = inp()
while t:
    t -= 1
    a = st1()
    oe = []
    c = 0
    for i in a:
        if i == '1':
            c += 1
        elif c != 0:
            oe.append(c)
            c = 0
    if c:
        oe.append(c)
    s = 0
    oe.sort(reverse=True)
    for i in range(len(oe)):
        if i % 2 == 0:
            s += oe[i]
    print(s)
