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


def VI(): return list(map(int, input().split()))


def main(info=0):
    a, b = VI()
    c, d = VI()

    detA = a * d - b * c

    denom = max(abs(a + b + c + d), abs(a + d - c - b),
                abs(a + c - b - d), abs(a + b - c - d))
    ans = 0 if detA == 0 else abs(detA / denom)
    print(ans)


def __starting_point():
    main()


__starting_point()
