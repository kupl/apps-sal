import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


(w1, h1, w2, h2) = mapin()
ans = 2 * (h1 + h2) + 2 * w1 + 4
print(ans)
