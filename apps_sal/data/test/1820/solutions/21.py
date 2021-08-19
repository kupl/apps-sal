import sys
import math
from functools import reduce
import bisect


def getN():
    return int(input())


def getNM():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


def input():
    return sys.stdin.readline().rstrip()


def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return False


for _ in range(int(input())):
    n = getN()
    arr = getList()
    if arr[0] + arr[1] <= arr[-1]:
        print(1, 2, n)
    else:
        print(-1)
