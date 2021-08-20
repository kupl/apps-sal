import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


(a, b, c) = mapin()
print(2 * min(a, b) + 2 * c + (abs(a - b) > 0))
