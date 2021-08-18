import itertools
import math
import collections as col
import sys
input = sys.stdin.readline


def getInts():
    return [int(s) for s in input().split()]


def getInt():
    return int(input())


def getStrs():
    return [s for s in input().split()]


def getStr():
    return input().strip()


def listStr():
    return list(input().strip())


"""
"""


def solve():
    N, X = getInts()
    if N <= 2:
        return 1
    N -= 3
    return N // X + 2


for _ in range(getInt()):
    print(solve())
