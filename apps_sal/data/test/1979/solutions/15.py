
# Below is Pythone code for input/output
# comment this out when submiting

import sys
from collections import Counter


# utils
def read_ints():
    return [int(i) for i in input().strip().split()]


def solve():
    # solves one test case
    pass


def intersection(left, right, mn, mx):
    # return [left, right ] or None
    if right < mn or left > mx:
        return None
    else:
        return [max(left, mn), min(right, mx)]


def main():
    n = int(input())
    a = read_ints()
    b = read_ints()
    # get all the diffs then find the mode
    # make dict of val to index
    # lineer pass to get diff array
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
