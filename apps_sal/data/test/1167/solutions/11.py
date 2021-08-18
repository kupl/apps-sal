import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())
def intin(): return int(input())


for _ in range(intin()):
    a, b, c, d, k = mapin()
    npen = math.ceil(a / c)
    npencil = math.ceil(b / d)
    if npen + npencil <= k:
        print(npen, npencil)
    else:
        print(-1)
