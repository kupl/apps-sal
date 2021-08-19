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


(N, B) = readmap()
A = readlist()
even = 0
odd = 0
cost = []
for i in range(0, N - 1):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    if even == odd:
        cost.append(abs(A[i] - A[i + 1]))
cost.sort()
ans = 0
for c in cost:
    if c > B:
        break
    else:
        ans += 1
        B -= c
print(ans)
