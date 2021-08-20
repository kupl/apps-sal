import bisect
import collections
import copy
import heapq
import itertools
import math
import numpy
import string
import sys
from operator import itemgetter


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


(N, M) = LI()
A = [LI() for _ in range(N)]
m = [[0] * 3 for _ in range(8)]
for c in range(4):
    A.sort(key=lambda x: ((c >> 2 & 1) * 2 - 1) * x[0] + ((c >> 1 & 1) * 2 - 1) * -1 * x[1] + ((c & 1) * 2 - 1) * x[2])
    for i in range(M):
        for j in range(3):
            m[c * 2][j] += A[i][j]
            m[c * 2 + 1][j] += A[N - 1 - i][j]
print(max([abs(x[0]) + abs(x[1]) + abs(x[2]) for x in m]))
