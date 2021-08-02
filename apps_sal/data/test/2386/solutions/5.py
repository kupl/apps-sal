import sys
import math
import itertools
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

    neg = []
    pos = []
    for i in range(N):
        num = A[i] - i - 1
        if num >= 0:
            pos.append(num)
        else:
            neg.append(-num)
    pos.sort()
    neg.sort()
    pos_l = len(pos)
    neg_l = len(neg)
    pos2 = [0] + deepcopy(pos)
    neg2 = [0] + deepcopy(neg)
    for i in range(1, pos_l + 1):
        pos2[i] += pos2[i - 1]
    for i in range(1, neg_l + 1):
        neg2[i] += neg2[i - 1]

    ans = float('inf')

    for i in range(pos_l):
        num = pos[i]
        res = i * num - pos2[i]
        res += (pos2[pos_l] - pos2[i + 1]) - num * (pos_l - 1 - i)
        res += neg2[neg_l] + num * neg_l
        ans = min(res, ans)

    for i in range(neg_l):
        num = neg[i]
        res = i * num - neg2[i]
        res += (neg2[neg_l] - neg2[i + 1]) - num * (neg_l - 1 - i)
        res += pos2[pos_l] + num * pos_l
        ans = min(res, ans)
    print(ans)


def __starting_point():
    main()


__starting_point()
