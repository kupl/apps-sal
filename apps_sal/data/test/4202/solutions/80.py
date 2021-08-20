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
    S = set()
    (L, R) = MI()
    mod = 2019
    if R // mod > (L - 1) // mod:
        print(0)
        return
    l = [i % mod for i in range(L, R + 1)]
    ans = float('inf')
    N = len(l)
    for index in range(N):
        for index2 in range(index + 1, N):
            ans = min(ans, l[index] * l[index2] % mod)
    print(ans)


def __starting_point():
    main()


__starting_point()
