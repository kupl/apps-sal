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


def main():
    (A, B, H, M) = MI()
    pai = math.pi
    h = H / 12 + M / 720
    m = M / 60
    angle = abs(h - m)
    if angle > 0.5:
        angle = 1 - angle
    res = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(360 * angle))
    print(math.sqrt(res))


def __starting_point():
    main()


__starting_point()
