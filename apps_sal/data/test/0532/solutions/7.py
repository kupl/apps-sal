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
    r = 0
    s = input()
    c = 0
    ai = ord('a')
    t = 0
    for si in s:
        sc = ord(si) - ai
        if sc > c:
            t = min(26 + c - sc, sc - c)
        else:
            t = min(c - sc, sc + 26 - c)
        r += t
        c = sc
    return r


print(f())
