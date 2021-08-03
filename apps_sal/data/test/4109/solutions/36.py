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
    N, M, X = MI()
    res = float('inf')
    D = Init(2**N, M, 0)
    C = defaultdict(int)
    L = [LI() for i in range(N)]
    for i in range(2**N):
        for j in range(N):
            if i >> j & 1 == 1 or C[i | 1 << j] > 0:
                continue
            for index, n in enumerate(L[j][1:]):
                D[i | 1 << j][index] = D[i][index] + n
            C[i | 1 << j] = C[i] + L[j][0]
    for i in range(1, 2**N):
        temp = D[i]
        ans = True
        for j in temp:
            if j < X:
                ans = False
                break
        if ans:
            res = min(res, C[i])
    if res == float('inf'):
        print(-1)
    else:
        print(res)


def __starting_point():
    main()


__starting_point()
