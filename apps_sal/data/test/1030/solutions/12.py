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


def main(n, p, k):
    x = range(p - k, p + k + 1)
    x = [j for j in x if j >= 1 and j <= n]
    if 1 not in x:
        print('<< ', end='')
    for j in range(max(1, p - k), p):
        print(str(j), end=' ')
    print('(' + str(p) + ') ', end='')
    for j in range(p + 1, min(p + k, n) + 1):
        print(str(j), end=' ')
    if n not in x:
        print('>>')


def main_input(info=0):
    (n, p, k) = map(int, input().split())
    main(n, p, k)


def __starting_point():
    main_input()


__starting_point()
