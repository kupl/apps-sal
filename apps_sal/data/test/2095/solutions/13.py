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


def main(a, n):
    s = []
    if n == 1:
        print(1)
        print(1)
        return
    for i in range(n):
        if 1 in a[i] or 3 in a[i]:
            continue
        s += [i + 1]
    print(len(s))
    print(' '.join([str(i) for i in s]))


def main_input(info=0):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    main(a, n)


def __starting_point():
    main_input()


__starting_point()
