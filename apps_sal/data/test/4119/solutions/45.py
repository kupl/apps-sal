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
    L = sorted(LI())
    L2 = []
    past = L[0]

    if M == 1:
        print(0)
        return

    for i in L[1:]:
        L2.append(i - past)
        past = i

    L2.sort(reverse=True)
    res = sum(L2)
    num = N - 1

    if num >= M:
        num = M - 1

    for i in range(num):
        res -= L2[i]

    print(res)


def __starting_point():
    main()


__starting_point()
