# -*- coding: utf-8 -*-
import sys
# from operator import itemgetter
# from fractions import gcd
# from math import ceil, floor
# from copy import deepcopy
# from itertools import accumulate
from collections import deque
# import math
# from functools import reduce
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return list(map(int, input().rstrip().split()))
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# BEGIN CUT HERE


class BIT:
    def __init__(self, x, d=0):
        if isinstance(x, int):
            self.size = x
            self.tree = [d for _ in range(self.size + 1)]
        elif isinstance(x, list):
            self.size = len(x)
            self.tree = [d for _ in range(self.size + 1)]
            self.build(x)
        else:
            raise TypeError

    def build(self, arr):
        if not isinstance(arr, list):
            raise TypeError
        for num, x in enumerate(arr):
            self.add0(num, x)

    def sum(self, i):
        s = self.tree[0]
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

    def add(self, i, a):
        if(i == 0):
            return
        while (i <= self.size):
            self.tree[i] += a
            i += (i & -i)

    def bisect_left(self, w):
        if w <= 0:
            return 0
        x = 0
        r = 1
        while (r < self.size):
            r <<= 1
        k = r
        while (k > 0):
            if x + k <= self.size and self.tree[x + k] < w:
                w -= self.tree[x + k]
                x += k
            k >>= 1
        return x + 1

    def query(self, l, r):
        return self.sum(r - 1) - self.sum(l - 1)

    def sum0(self, i):
        return self.sum(i + 1)

    def add0(self, i, a):
        self.add(i + 1, a)

    def query0(self, l, r):
        return self.sum(r) - self.sum(l)

    def __getitem__(self, item):
        _tmp = item.indices(self.size + 1)
        return [self.sum(i) - self.sum(i - 1) for i in range(_tmp[0], _tmp[1], _tmp[2])]

    def __str__(self):
        return str(self[1:self.size + 1])

# END CUT


def main():
    n = ii()
    a = lmi()
    q = ii()
    bit = BIT(a)
    # print(bit)
    for i in range(q):
        l, r = mi()
        a = bit.query(l, r + 1)
        print((a - a % 10) // 10)


def __starting_point():
    main()


__starting_point()
