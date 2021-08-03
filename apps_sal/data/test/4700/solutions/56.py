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
    N, M = MI()
    H = LI()
    G = [[] for i in range(N)]
    for i in range(M):
        a, b = MI()
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    res = [-1] * N
    for i in range(N):
        if res[i] != -1:
            continue
        h = H[i]
        ans = True
        for index in G[i]:
            temp_H = H[index]
            if h > temp_H:
                res[index] = 0
            else:
                ans = False
                break
        if ans:
            res[i] = 1
        else:
            res[i] = 0
    ans = 0
    for i in res:
        if i != 0:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
