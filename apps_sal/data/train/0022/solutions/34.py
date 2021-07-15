from sys import stdin, stdout
import heapq
import cProfile, math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect, bisect_right
import itertools
from copy import deepcopy
from fractions import Fraction
import sys, threading
import operator as op
from functools import reduce
import sys


def get_int():
    return int(stdin.readline().strip())


def get_tuple():
    return list(map(int, stdin.readline().split()))


def get_list():
    return list(map(int, stdin.readline().split()))


def solve():
    n,k = get_tuple()
    n = str(n)
    while '0' not in n and k>1:
        n = int(n) + int(max(n))*int(min(n))
        n = str(n)
        k -= 1
    return n


def main():
    ans = solve()
    print(ans)

TestCases = True

if TestCases:
    for i in range(get_int()):
        main()
else:
    main()

