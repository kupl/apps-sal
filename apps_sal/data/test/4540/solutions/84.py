import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
A = zz()
A.append(0)
diff = [0] * N
prev = 0
A_ = [0]
A_.extend(A)
sum_ = 0
for i in range(len(A_) - 1):
    sum_ += abs(A_[i] - A_[i + 1])

for i in (range(1, N + 1)):
    sub = abs(A_[i] - A_[i - 1]) + abs(A_[i] - A_[i + 1])
    add = abs(A_[i - 1] - A_[i + 1])
    print(sum_ + add - sub)
