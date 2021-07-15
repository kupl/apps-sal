from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


# B
N, M = readmap()
A = [0] + readlist() + [M]

on_time = []
off_time = []
for i in range(1, N+2):
    if i % 2 == 1:
        on_time.append(A[i] - A[i - 1])
    else:
        off_time.append(A[i] - A[i - 1])

sum_on_time = sum(on_time)
max_on_time = sum_on_time
if N % 2 == 1:
    i = N + 1
    while i > 0:
        if A[i] - A[i - 1] > 1:
            x = A[i - 1] + 1
            max_on_time = max(max_on_time, sum_on_time + A[i] - x)
        sum_on_time = sum_on_time + (A[i] - A[i - 1]) - (A[i - 1] - A[i - 2])

        if A[i - 1] - A[i - 2] > 1:
            x = A[i - 1] - 1
            max_on_time = max(max_on_time, sum_on_time + x - A[i - 2])

        i -= 2

    print(max_on_time)
else:
    i = N
    sum_on_time -= A[N + 1] - A[N]
    while i > 0:
        if A[i] - A[i - 1] > 1:
            x = A[i - 1] + 1
            max_on_time = max(max_on_time, sum_on_time + A[i] - x)
        sum_on_time = sum_on_time + (A[i] - A[i - 1]) - (A[i - 1] - A[i - 2])

        if A[i - 1] - A[i - 2] > 1:
            x = A[i - 1] - 1
            max_on_time = max(max_on_time, sum_on_time + x - A[i - 2])

        i -= 2

    print(max_on_time)
