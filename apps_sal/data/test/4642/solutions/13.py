import bisect
import copy
import fractions
import functools
import heapq
import math
import random
import sys


def __starting_point():

    T = int(input())

    for t in range(T):
        N, X, Y = tuple(map(int, input().split()))

        for div in range(1, (Y - X) + 1):
            if (Y - X) % div == 0 and div * (N - 1) >= (Y - X):
                break

        max_ = Y
        n = N - math.ceil(Y / div)
        while n > 0:
            max_ += div
            n -= 1

        print(' '.join(str(max_ - (i * div)) for i in range(N)))


__starting_point()
