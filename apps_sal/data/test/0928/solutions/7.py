"""
研究室PCでの解答
"""
import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
alp = 'abcdefghijklmnopqrstuvwxyz'


def main():
    (n, k) = list(map(int, ipt().split()))
    a = [int(i) for i in ipt().split()]
    ans = 0
    sm = 0
    l = 0
    for i in range(n):
        sm += a[i]
        while sm >= k:
            sm -= a[l]
            l += 1
        ans += l
    print(ans)
    return None


def __starting_point():
    main()


__starting_point()
