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

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7


def f():
    a = list(map(int, input().split()))
    a.sort()

    return a[1] - a[0] + a[2] - a[1]


print(f())
