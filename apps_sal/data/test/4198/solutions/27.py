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
    A, B, X = MI()
    keta = 0

    while True:
        temp = A * pow(10, keta) + B * (keta + 1)
        if temp > X:
            break
        keta += 1
    keta -= 1

    if A + B > X:
        print(0)
        return

    ans = (X - B * (keta + 1)) // A

    if len(str(ans)) > keta + 1:
        ans = int("9" * (keta + 1))

    if ans >= 1000000000:
        print(1000000000)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
