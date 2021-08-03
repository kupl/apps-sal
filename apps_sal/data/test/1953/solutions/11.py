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


def main(n, s):
    s.sort()
    curr = 0
    ans = 0
    for x in s:
        if x >= curr:
            ans += 1
            curr += x
    print(ans)


def main_input(info=0):
    n = int(input())
    t = list(map(int, input().split()))
    main(n, t)


def __starting_point():
    main_input()


__starting_point()
