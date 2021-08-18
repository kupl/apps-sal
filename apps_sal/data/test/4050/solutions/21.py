
import math
import os
import random
import re
import sys
from collections import defaultdict


def find_max_non_intersecting(segments):
    n = len(segments)

    r = -1
    result = []
    for i in range(n):
        a, b = segments[i]
        if a > r:
            result.append((a, b))
            r = b

    return result


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))

    s = []
    for ai in a:
        s.append((s[-1] if s else 0) + ai)

    d = defaultdict(list)
    for j in range(n):
        for i in range(j + 1):
            d[s[j] - (s[i - 1] if i - 1 >= 0 else 0)].append((i, j))

    vals = []
    for v in d.values():
        non_inters = find_max_non_intersecting(v)
        if len(non_inters) > len(vals):
            vals = non_inters

    print(len(vals))
    for l, r in vals:
        print(l + 1, r + 1)


__starting_point()
