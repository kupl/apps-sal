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
    A = LI()
    A2 = []
    for i in range(N):
        A2.append([i + 1, A[i]])
    A2.sort(key=lambda x: x[1])
    ans = ""
    for a, b in A2:
        ans += str(a) + " "
    print(ans)


def __starting_point():
    main()


__starting_point()
