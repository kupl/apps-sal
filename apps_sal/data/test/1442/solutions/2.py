import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

# Guide:
#   1. construct complex data types while reading (e.g. graph adj list)
#   2. avoid any non-necessary time/memory usage
#   3. avoid templates and write more from scratch
#   4. switch to "flat" implementations


def VI(): return list(map(int, input().split()))
def I(): return int(input())
def LIST(n, m=None): return [0] * n if m is None else [[0] * m for i in range(n)]


def main(info=0):
    n, s = VI()
    d, p, q = LIST(n), LIST(n), LIST(n)
    db = {}
    ds = {}
    for i in range(n):
        d[i], p[i], q[i] = input().split()
    p = [int(x) for x in p]
    q = [int(x) for x in q]
    for i in range(n):
        if d[i] == 'B':
            if p[i] in db:
                db[p[i]] = db[p[i]] + q[i]
            else:
                db[p[i]] = q[i]
        if d[i] == 'S':
            if p[i] in ds:
                ds[p[i]] = ds[p[i]] + q[i]
            else:
                ds[p[i]] = q[i]
    lb = sorted(list(db.items()))[::-1][:s]
    ls = sorted(list(ds.items()))[:s][::-1]

    for k, v in ls:
        print("S {} {}".format(k, v))
    for k, v in lb:
        print("B {} {}".format(k, v))


def __starting_point():
    main()


__starting_point()
