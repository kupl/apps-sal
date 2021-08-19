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


def main(n, t, a):
    j = 1
    while j < n:
        # print(j,a[j-1])
        j += a[j - 1]
        if j == t:
            print("YES")
            return
    print("NO")


def main_input():
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    main(n, t, a)


def __starting_point():
    main_input()


__starting_point()
