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
    (N, M, Q) = MI()
    L = [LI() for i in range(Q)]
    A = [i for i in range(1, M + 1)]
    ans = 0
    for i in itertools.combinations_with_replacement(A, N):
        temp = 0
        for (a, b, c, d) in L:
            if i[b - 1] - i[a - 1] == c:
                temp += d
        if temp > ans:
            ans = temp
    print(ans)


def __starting_point():
    main()


__starting_point()
