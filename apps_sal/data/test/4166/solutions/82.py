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
    (N, M) = MI()
    L = ['-1'] * N
    for i in range(M):
        (s, c) = MI()
        s -= 1
        c = str(c)
        if L[s] == '-1':
            L[s] = c
        elif L[s] != c:
            print(-1)
            return
    if L[0] == '0' and N >= 2:
        print(-1)
        return
    elif (L[0] == '0' or L[0] == '-1') and N == 1:
        print(0)
        return
    elif L[0] == '-1':
        L[0] = '1'
    L = ['0' if L[i] == '-1' else L[i] for i in range(N)]
    print(''.join(L))


def __starting_point():
    main()


__starting_point()
