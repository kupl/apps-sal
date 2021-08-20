import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
input = sys.stdin.readline


def RD():
    return input().rstrip()


def F():
    return float(input().rstrip())


def I():
    return int(input().rstrip())


def MI():
    return map(int, input().split())


def MF():
    return map(float, input().split())


def LI():
    return list(map(int, input().split()))


def TI():
    return tuple(map(int, input().split()))


def LF():
    return list(map(float, input().split()))


def Init(H, W, num):
    return [[num for i in range(W)] for j in range(H)]


def main():
    N = input().rstrip()
    A = LI()
    if A[0] > 0:
        A1 = 0
        B1 = A[0]
        A2 = A[0] + 1
        B2 = -1
    elif A[0] == 0:
        A1 = 1
        B1 = 1
        A2 = 1
        B2 = -1
    else:
        A1 = -A[0] + 1
        B1 = 1
        A2 = 0
        B2 = A[0]
    for num in A[1:]:
        if B1 > 0:
            B1 += num
            if B1 > 0:
                A1 += B1 + 1
                B1 = -1
            elif B1 == 0:
                A1 += 1
                B1 = -1
        else:
            B1 += num
            if B1 < 0:
                A1 += -B1 + 1
                B1 = 1
            elif B1 == 0:
                B1 = 1
                A1 += 1
    for num in A[1:]:
        if B2 > 0:
            B2 += num
            if B2 > 0:
                A2 += B2 + 1
                B2 = -1
            elif B2 == 0:
                A2 += 1
                B2 = -1
        else:
            B2 += num
            if B2 < 0:
                A2 += -B2 + 1
                B2 = 1
            elif B2 == 0:
                B2 = 1
                A2 += 1
    print(min(A1, A2))


def __starting_point():
    main()


__starting_point()
