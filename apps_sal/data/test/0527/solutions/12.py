from collections import defaultdict
from bisect import bisect_left


def solve(s, t):
    dd = defaultdict(list)
    for i, c in enumerate(s):
        dd[c].append(i)
    inv = 0
    index = 0
    for c in t:
        x = bisect_left(dd[c], index)
        if x == len(dd[c]):
            inv += 1
            if not dd[c]:
                return -1
            index = dd[c][0] + 1
        else:
            index = dd[c][x] + 1
    return len(s) * inv + index


def main():
    s = input()
    t = input()
    print((solve(s, t)))


def __starting_point():
    main()


__starting_point()
