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
    N = I()
    D = defaultdict(int)
    for i in range(N):
        D[input().rstrip()] += 1
    D = D.items()
    D = sorted(D, key=lambda x: x[0])
    D = sorted(D, key=lambda x: x[1], reverse=True)
    num = D[0][1]

    for key, n in D:
        if n != num:
            return
        print(key)


def __starting_point():
    main()


__starting_point()
