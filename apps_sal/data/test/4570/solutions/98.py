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


(N, A, B) = LI()
x = N * A
y = B
if x <= y:
    print(x)
else:
    print(y)
