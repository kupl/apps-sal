from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


n = read()
W = []
H = []
for _ in range(n):
    w, h = readmap()
    W.append(w)
    H.append(h)

height = max(W[0], H[0])
for i in range(1, n):
    w, h = W[i], H[i]
    if w > height and h > height:
        print("NO")
        quit()
    elif w > height:
        height = h
    elif h > height:
        height = w
    else:
        height = max(h, w)

print("YES")
