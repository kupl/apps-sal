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


def main(a, b, c, d, info=0):
    i = max(3 * a // 10, a - a // 250 * c)
    j = max(3 * b // 10, b - b // 250 * d)
    if i == j:
        print("Tie")
    elif i > j:
        print("Misha")
    else:
        print("Vasya")


def main_input(info=0):
    a, b, c, d = list(map(int, input().split()))
    main(a, b, c, d, info=info)


def __starting_point():
    main_input()


__starting_point()
