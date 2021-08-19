from copy import deepcopy
import itertools
from bisect import bisect_left


def read():
    return int(input())


def readmap():
    return list(map(int, input().split()))


def readlist():
    return list(map(int, input().split()))


color = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
gem = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
N = int(input())
s = set()
for _ in range(N):
    s.add(input())
m = 6 - N
print(m)
for i in range(6):
    if not color[i] in s:
        print(gem[i])
