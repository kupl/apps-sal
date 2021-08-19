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
    (N, K) = MI()
    D = deque()
    D.append(1)
    num = 1
    index = 0
    while num <= K:
        num *= 2
        index += 1
        D.append(num)
    ans = 0
    for i in range(1, N + 1):
        temp = K / i
        index2 = bisect_left(D, temp)
        ans += D[index - index2]
    print(ans / (N * D[index]))


def __starting_point():
    main()


__starting_point()
