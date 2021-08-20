import sys
import math
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
    S = input().rstrip()
    T = input().rstrip()
    L = [[S[i], T[i]] for i in range(len(S))]
    L.sort(key=lambda x: x[0])
    D = defaultdict(int)
    D2 = defaultdict(int)
    for (a, b) in L:
        if (D[a] == 0 or D[a] == b) and (D2[b] == 0 or D2[b] == a):
            D[a] = b
            D2[b] = a
        else:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
