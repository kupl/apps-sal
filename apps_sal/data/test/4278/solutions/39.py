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
    N = I()
    L = []
    for i in range(N):
        temp = input().rstrip()
        temp = sorted(temp)
        L.append(temp)
    for i in range(9, -1, -1):
        L.sort(key=lambda x: x[i])
    ans = 0
    index = 0
    temp_index = 0
    while True:
        while index + 1 < N and L[index + 1] == L[index]:
            index += 1
            temp_index += 1
        ans += (temp_index + 1) * temp_index // 2
        temp_index = 0
        index += 1
        if index >= N - 1:
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
