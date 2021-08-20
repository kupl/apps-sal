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
        N = int(input())
        A = list(map(int, input().split()))
        total = 0
        min_ = 0
        for a in A:
            total += a
            min_ = min(min_, total)
        print(str(abs(min_)))


__starting_point()
