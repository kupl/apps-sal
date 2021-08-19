from copy import deepcopy
import itertools
from bisect import bisect_left
import math


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


(x, y) = readmap()
if y * math.log(x) < x * math.log(y):
    print('<')
elif y * math.log(x) > x * math.log(y):
    print('>')
else:
    print('=')
