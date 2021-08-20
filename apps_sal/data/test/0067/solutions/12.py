import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


(x, y, z) = mapin()
if x == y and z == 0:
    print(0)
elif abs(x - y) > z:
    if x - y > 0:
        print('+')
    else:
        print('-')
else:
    print('?')
