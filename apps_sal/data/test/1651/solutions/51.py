import copy
import math
import time
import statistics
import math
import itertools
import bisect
import sys
from decimal import *
from collections import deque


def get_int():
    return int(input())


def get_string():
    return input()


def get_int_list():
    return [int(x) for x in input().split()]


def get_string_list():
    return input().split()


def get_int_multi():
    return list(map(int, input().split()))


def get_string_char_list():
    return list(str(input()))


sys.setrecursionlimit(10 ** 6)


def main():
    start = time.time()
    (s, p) = get_int_multi()
    m1 = (s + (s ** 2 - 4 * p) ** (1 / 2)) / 2
    m2 = (s - (s ** 2 - 4 * p) ** (1 / 2)) / 2
    if round(m1) == m1 and round(m2) == m2 and (m1 > 0) and (m2 > 0):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
