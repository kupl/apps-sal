import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque


def VI():
    return list(map(int, input().split()))


def main(n, l, r, x, c):
    all = []
    for i in range(1, n + 1):
        com = combinations(c, i)
        for j in com:
            s = sum(j)
            if s >= l and s <= r and (max(j) - min(j) >= x):
                all.append(j)
    print(len(all))


def main_input(info=0):
    (n, l, r, x) = VI()
    c = VI()
    main(n, l, r, x, c)


def __starting_point():
    main_input()


def test():
    (n, l, r, x) = (15, 1, 100000, 1)
    c = list(range(15))
    main(n, l, r, x, c)


__starting_point()
