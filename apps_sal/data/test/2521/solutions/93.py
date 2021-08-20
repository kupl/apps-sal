import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools
from collections import deque
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def main():
    N = I()
    A = LI()
    wakeme = N
    Aleftsum = [0 for _ in range(3 * N + 1)]
    Arightsum = [0 for _ in range(3 * N + 1)]
    leftA = [x for x in A[:N]]
    rightA = [-x for x in A[-N:]]
    heapq.heapify(leftA)
    heapq.heapify(rightA)
    lsum = sum(leftA)
    rsum = sum(rightA)
    Aleftsum[wakeme] = lsum
    Arightsum[2 * N] = -rsum
    for i in range(N):
        newl = A[wakeme + i]
        lsum += newl
        lsum -= heapq.heappushpop(leftA, newl)
        Aleftsum[wakeme + i + 1] = lsum
        newr = A[2 * N - 1 - i]
        rsum -= newr
        rsum -= heapq.heappushpop(rightA, -newr)
        Arightsum[2 * N - 1 - i] = -rsum
    ans = -inf
    for i in range(N, 2 * N + 1):
        ans = max(ans, Aleftsum[i] - Arightsum[i])
    print(ans)


main()
