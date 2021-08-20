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


def gcd2(i, past):
    return i * past // math.gcd(i, past)


def main():
    (A, B, C, D) = MI()
    AC = (A - 1) // C
    BC = B // C
    AD = (A - 1) // D
    BD = B // D
    ACD = (A - 1) // gcd2(C, D)
    BCD = B // gcd2(C, D)
    ans = BC + BD - BCD - (AC + AD - ACD)
    print(B - A + 1 - ans)


def __starting_point():
    main()


__starting_point()
