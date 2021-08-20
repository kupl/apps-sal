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


(A, B, C, D) = LI()
if A + B > C + D:
    print('Left')
elif A + B == C + D:
    print('Balanced')
else:
    print('Right')
