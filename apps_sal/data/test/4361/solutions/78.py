import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush

input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]


def main():
    N, K = MI()
    L = [I() for i in range(N)]
    L.sort()
    res = float('inf')

    for i in range(N - K + 1):
        res = min(res, L[i + K - 1] - L[i])

    print(res)


def __starting_point():
    main()


__starting_point()
