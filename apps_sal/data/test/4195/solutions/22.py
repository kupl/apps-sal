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
import copy
import functools
from collections import deque
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def main():
    (D, N) = LI()
    cnt = 0
    num = 0
    for i in range(1, 10 ** 7 + 1):
        if i % 100 ** D == 0 and i % 100 ** (D + 1) > 0:
            cnt += 1
        if cnt == N:
            num = i
            break
    print(num)


main()
