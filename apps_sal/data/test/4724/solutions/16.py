import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def I():
    # 1 line 1 int
    return int(sys.stdin.readline().rstrip())


def LI():
    # 1 line n int
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    # 1 line 1 string
    return sys.stdin.readline().rstrip()


def LS():
    # 1 line n strings
    return list(sys.stdin.readline().rstrip().split())


R = I()
G = I()

x = 2 * G - R
print(x)
