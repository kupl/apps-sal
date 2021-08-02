import sys
from copy import deepcopy
import numpy as np
readline = sys.stdin.readline
read = sys.stdin.read


def main():
    n = int(readline())
    a = np.array([list(map(int, l.split())) for l in read().splitlines()])
    cost = deepcopy(a)
    for k in range(n):
        arr = np.stack([cost, [cost[k]] + np.transpose([cost[k]])])
        cost = np.amin(arr, axis=0)
    f = np.sum(cost < a)
    if f:
        print((-1))
        return
    filt = np.sum([([cost[k]] + np.transpose([cost[k]])) == cost for k in range(n)], axis=0) == 2
    print((np.sum(a[filt]) // 2))


def __starting_point():
    main()


__starting_point()
