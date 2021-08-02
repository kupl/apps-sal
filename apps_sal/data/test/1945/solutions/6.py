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
from collections import defaultdict


def main2(n, old, new):
    orig = []
    visited = []

    o = []
    l = []

    for i, j in zip(old, new):
        if i not in visited:
            orig.append([i, j])
            visited.append(j)
        else:
            for k, v in enumerate(orig):
                if i == v[-1]:
                    orig[k].append(j)
                    visited.append(j)
                    continue
    print(len(orig))
    for v in orig:
        print(v[0], " ", v[-1])


def main(n, old, new):
    o = []
    l = []
    for i, j in zip(old, new):
        if i not in l:
            o.append(i)
            l.append(j)
        else:
            k = l.index(i)
            l[k] = j
    print(len(o))
    for x, y in zip(o, l):
        print(x, y)


def main_input(info=0):
    n = int(input())
    l, r = list(range(n)), list(range(n))
    for i in range(n):
        l[i], r[i] = input().split()
    main(n, l, r)


def __starting_point():
    main_input()


__starting_point()
