from sys import stdin as Si, maxsize as m
from math import floor as F
from collections import defaultdict as dt
from operator import itemgetter as ig
from math import pi


def __starting_point():
    n = int(Si.readline())
    a = list(map(int, Si.readline().split()))
    (s, d) = (0, {})
    for x in a:
        s += x
        d[s] = d.get(s, 0) + 1
    print(n - max([d[k] for k in d]))


__starting_point()
