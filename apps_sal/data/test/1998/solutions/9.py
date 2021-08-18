import heapq
from itertools import groupby


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(ll):
    return sum(1 for _ in ll)


def solve():
    """
    13 3 2 3
    1000000010001
        3     1
    000000000
      a, b

    - how many shots do you need to reduce maximum possible number of ships in a segment?
    1 1 1 0
    0
    """
    n, a, b, k = read_ints()
    s = input().strip()
    segments = []
    maximum_count = 0
    for start, vals in groupby(enumerate(s), key=lambda p: p[1]):
        val = next(vals)
        if val[1] == '0':
            segments.append((val[0], 1 + ilen(vals)))
            maximum_count += segments[-1][1] // b
    shots = []
    while maximum_count >= a:
        start, length = segments.pop()
        if length // b > 0:
            shots.append(start + b - 1)
            segments.append((start + b, length - b))
            maximum_count -= 1
    print(len(shots))
    print(' '.join([str(shot + 1) for shot in shots]))


def __starting_point():
    solve()


__starting_point()
