'''
研究室PCでの解答
'''
import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9 + 7


def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    p2 = [0] * (n + 1)
    for i in range(n, 0, -1):
        sm = 0
        for j in range(i, n + 1, i):
            sm += p2[j]
        p2[i] = (a[i - 1] - sm) % 2

    sm = sum(p2)
    print(sm)
    ans = []
    for i, pi in enumerate(p2):
        if pi:
            ans.append(str(i))

    print((" ".join(ans)))
    return None


def __starting_point():
    main()


__starting_point()
