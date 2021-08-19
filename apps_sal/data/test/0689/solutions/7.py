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
    n = inp()
    co = [0] * 26
    for i in range(n):
        s = st1()
        for j in s:
            co[ord(j) - 97] += 1
    fl = 0
    for i in range(26):
        if co[i] % n == 0:
            continue
        fl = 1
    s = 'YES'
    if fl:
        s = 'NO'
    print(s)
