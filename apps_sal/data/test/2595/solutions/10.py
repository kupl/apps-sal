from collections import defaultdict as dd
import math
import sys
import string
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()
for _ in range(q):
    a, b = mi()

    small = min(a, b)
    big = max(a, b)
    ops = 0
    while small < big:
        small *= 2
        ops += 1
    if small == big:
        print((ops + 2) // 3)
    else:
        print(-1)
