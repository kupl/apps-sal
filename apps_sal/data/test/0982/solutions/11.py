from math import *
from collections import Counter, defaultdict


def I():
    return int(input())


def M():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


for _ in range(I()):
    (a, b) = M()
    if 2 * a > b:
        print('YES')
    else:
        print('NO')
