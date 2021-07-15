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


N, K = readmap()
A = readlist()

idx = []

for i in range(N):
    if A[i] not in A[:i]:
        idx.append(i+1)
    if len(idx) == K:
        break

if len(idx) == K:
    print("YES")
    print(" ".join(list(map(str, idx))))
else:
    print("NO")
