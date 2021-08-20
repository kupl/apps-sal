from collections import defaultdict as dd
import math
import sys
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
    (x1, y1, x2, y2) = mi()
    if x1 == x2 or y1 == y2:
        print(1)
    else:
        r = x2 - x1 + y2 - y1
        picks = x2 - x1
        diff = r - picks
        lower = picks * (picks - 1) // 2
        upper = r * (r - 1) // 2 - (r - picks) * (r - picks - 1) // 2
        print(upper - lower + 1)
