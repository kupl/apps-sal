import sys
import bisect as b
import math
from collections import defaultdict as dd
input = sys.stdin.readline
mo = 10**9 + 7


def cin():
    return list(map(int, sin().split()))


def ain():
    return list(map(int, sin().split()))


def sin():
    return input()


def inin():
    return int(input())


for i in range(inin()):
    a, b = cin()
    print(min(a, b, (a + b) // 3))
