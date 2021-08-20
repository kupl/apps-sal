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
    N = I()
    D = [[[], []] for i in range(N)]
    for i in range(N):
        a = I()
        for j in range(a):
            (x, y) = MI()
            if y == 1:
                D[i][0].append(x - 1)
            else:
                D[i][1].append(x - 1)
    visit = [0] * N
    res = 0
    A = [0, 1]
    for i in itertools.product(A, repeat=N):
        ans = True
        for (index, j) in enumerate(i):
            if j == 0:
                continue
            else:
                for k in D[index][0]:
                    if i[k] == 0:
                        ans = False
                        break
                for k in D[index][1]:
                    if i[k] == 1:
                        ans = False
                        break
        if ans:
            res = max(res, sum(i))
    print(res)


def __starting_point():
    main()


__starting_point()
