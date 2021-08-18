
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/13 20:48

"""


def solve(N, L, X, Y, A):
    vs = set(A)
    mx = any([a + X in vs for a in A])
    my = any([a + Y in vs for a in A])
    if mx and my:
        print(0)
    elif mx:
        print(1)
        print(Y)
    elif my:
        print(1)
        print(X)
    else:
        for a in vs:
            for b, c in [(a + X, Y), (a + Y, X), (a - X, Y), (a - Y, X)]:
                if 0 <= b <= L:
                    if (b + c <= L and b + c in vs) or (b - c >= 0 and b - c in vs):
                        print(1)
                        print(b)
                        return

        print(2)
        print('{} {}'.format(X, Y))


N, L, X, Y = map(int, input().split())
A = [int(x) for x in input().split()]
solve(N, L, X, Y, A)
