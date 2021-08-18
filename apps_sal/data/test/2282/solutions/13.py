import sys
import math
import heapq
import bisect
import re
from collections import deque
from decimal import *
from fractions import gcd

sys.setrecursionlimit(1000000000)


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


def modst(q, s):
    res = 1
    while s:
        if s % 2:
            res *= q
        q *= q
        s //= 2
    return res


def main():
    n = int(sys.stdin.readline())
    e = list(sys.stdin.readline())
    print(n + 1)


main()
