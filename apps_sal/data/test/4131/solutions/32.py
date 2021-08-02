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
    L = []

    for i in range(M):
        temp = [i] + LI()
        L.append(temp)
    L.sort(key=lambda x: x[2])
    L.sort(key=lambda x: x[1])
    ans = [0] * M
    D = defaultdict(int)
    for a, b, c in L:
        D[b] += 1
        c = D[b]
        ans[a] = str(b).zfill(6) + str(c).zfill(6)

    for i in ans:
        print(i)


def __starting_point():
    main()


__starting_point()
