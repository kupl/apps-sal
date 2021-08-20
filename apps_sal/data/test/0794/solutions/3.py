import math
from collections import deque, defaultdict
from sys import stdin, stdout


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


n = int(input())
a = listin()
a.sort()
if len(set(a)) == 1:
    print(-1)
else:
    print(*a)
