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
    N = I()
    for i in range(30):
        nokori = N - 7 * i
        if nokori >= 0 and nokori % 4 == 0:
            print('Yes')
            return
    print('No')
    return


main()
