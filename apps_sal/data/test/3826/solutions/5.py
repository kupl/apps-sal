import math
from collections import defaultdict


def try_solve(x, d):
    occ = defaultdict(lambda: 0)
    for i in range(d, len(x)):
        occ[x[i]] += 1
    multi = 0
    for (k, v) in list(occ.items()):
        if v > 1:
            multi += 1
    if multi == 0:
        return True
    if d == 0:
        return False
    for i in range(len(x) - d):
        occ[x[i]] += 1
        if occ[x[i]] == 2:
            multi += 1
        occ[x[i + d]] -= 1
        if occ[x[i + d]] == 1:
            multi -= 1
        if multi == 0:
            return True
    return False


def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    for i in range(n - 1):
        if try_solve(x, i):
            print(i)
            return
    print(n - 1)


def __starting_point():
    main()


__starting_point()
