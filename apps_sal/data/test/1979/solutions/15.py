

import sys
from collections import Counter


def read_ints():
    return [int(i) for i in input().strip().split()]


def solve():
    pass


def intersection(left, right, mn, mx):
    if right < mn or left > mx:
        return None
    else:
        return [max(left, mn), min(right, mx)]


def main():
    n = int(input())
    a = read_ints()
    b = read_ints()
    d = dict()
    for idx, i in enumerate(a):
        d[i] = idx
    diff = []
    for idx, i in enumerate(b):
        idx1 = d[i]
        delta = (idx1 - idx) % n
        diff.append(delta)
    data = Counter(diff)
    print(data.most_common(1)[0][1])


def __starting_point():
    main()


__starting_point()
