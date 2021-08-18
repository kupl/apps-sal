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


C1 = S()
C2 = S()

if C1[0] == C2[2] and C1[1] == C2[1] and C1[2] == C2[0]:
    print("YES")
else:
    print("NO")
