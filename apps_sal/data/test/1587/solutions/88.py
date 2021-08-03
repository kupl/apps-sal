import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9


def main():
    n = int(input())
    c = list(input())
    l, r = 0, len(c) - 1

    result = 0
    while r - l > 0:
        if c[l] == 'W' and c[r] == 'R':
            c[l], c[r] = c[r], c[l]
            result += 1
        if c[r] == 'W':
            r -= 1
        if c[l] == "R":
            l += 1
        # print(c)
    print(result)


def __starting_point():
    main()


__starting_point()
