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


def Eratosthenes(n):
    from math import sqrt
    res = [True] * (n + 1)
    res[0] = False
    res[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if res[i]:
            for j in range(2 * i, n + 1, i):
                res[j] = False
    return res


def main():
    X = I()
    n = pow(10, 6)
    res = Eratosthenes(n)

    while True:
        if res[X]:
            print(X)
            return

        X += 1


def __starting_point():
    main()


__starting_point()
