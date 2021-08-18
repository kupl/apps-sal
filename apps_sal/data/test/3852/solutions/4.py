import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)


def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    ma = max(a)
    mi = min(a)
    if mi * ma < 0:
        print((2 * (n - 1)))
        if abs(ma) > abs(mi):
            mk = a.index(ma)
            for i in range(n):
                if i == mk:
                    continue
                print((mk + 1, i + 1))
                a[i] += ma
        else:
            mk = a.index(mi)
            for i in range(n):
                if i == mk:
                    continue
                print((mk + 1, i + 1))
                a[i] += mi
    else:
        print((n - 1))
    ma = max(a)
    mi = min(a)
    if ma <= 0:
        for i in range(n - 1):
            print((n - i, n - i - 1))
    else:
        for i in range(n - 1):
            print((i + 1, i + 2))

    return


def __starting_point():
    main()


__starting_point()
