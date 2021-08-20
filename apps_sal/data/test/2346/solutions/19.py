from copy import deepcopy
from functools import reduce
from collections import Counter
import sys
sys.setrecursionlimit(2000)


def __starting_point():
    n = [int(val) for val in sys.stdin.readline().split()][0]
    tree = {i + 1: [[], []] for i in range(n)}
    for i in range(n):
        (p, c) = [int(val) for val in sys.stdin.readline().split()]
        tree[i + 1][0].append((p, c))
        if p != -1:
            tree[p][1].append((i, c))
    d = []
    for i in range(1, n + 1):
        (p, c) = tree[i]
        if p[0][1] == 1 and sum([x[1] for x in c]) == len(c):
            d.append(i)
    if len(d) == 0:
        print(-1)
    else:
        for val in d:
            print(val, end=' ')
        print('')


__starting_point()
