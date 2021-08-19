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
    return map(int, input().split())


def inp():
    return int(input())


def st1():
    return input().rstrip('\n')


t = inp()
while t:
    t -= 1
    n = inp()
    for i in range(1, n + 1):
        print(i, end=' ')
    print()
