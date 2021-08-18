import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


xs = LI()

if xs[0] == xs[1]:
    print(xs[2])
elif xs[0] == xs[2]:
    print(xs[1])
else:
    print(xs[0])
