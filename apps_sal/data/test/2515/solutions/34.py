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
def MI(): return list(map(int, input().split()))
def MF(): return list(map(float, input().split()))
def LI(): return list(map(int, input().split()))
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


class BIT():
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def rangesum(self, i, k):
        return self.sum(k) - self.sum(i)

    def lower_bound(self, x):
        if x <= 0:
            return 0
        else:
            i = 0
            r = 1
            while(r < self.n):
                r = r << 1
            len = r
            while len > 0:
                if(i + len < self.n and self.bit[i + len] < x):
                    x -= self.bit[i + len]
                    i += len
                len = len >> 1
            return i + 1


def main():
    max_num = 100000
    Q = I()
    S = Eratosthenes(max_num)
    bit = BIT(max_num)

    for a in range(1, max_num, 2):
        b = (a + 1) // 2
        if S[a] and S[b]:
            bit.add(a, 1)

    for q in range(Q):
        l, r = MI()
        print((bit.sum(r) - bit.sum(l - 1)))


def __starting_point():
    main()


__starting_point()
