import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)


def main():
    n = int(ipt())
    mod = 10**9 + 7
    a = [n, n * n % mod]
    sa = [0, 0]
    for i in range(2, n):
        a.append((a[-1] + sa[-1] + (n - i + 1) * n % mod) % mod)
        sa.append((sa[-1] + a[i - 2] + n - 1) % mod)

    print((a[-1]))

    return


def __starting_point():
    main()


__starting_point()
