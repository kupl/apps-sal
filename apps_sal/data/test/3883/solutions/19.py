import collections
import itertools
import fractions
import functools
import heapq
import math
import queue


def solve():
    (a, b) = list(map(int, input().split()))
    if a < b:
        return -1
    return (a + b) / (2 * ((a + b) // (2 * b)))


def __starting_point():
    print(solve())


__starting_point()
