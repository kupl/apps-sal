import collections as col
import math
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


'\n'


def solve():
    (A, B, C) = getInts()
    return A + B + C - 1


for _ in range(getInt()):
    print(solve())
