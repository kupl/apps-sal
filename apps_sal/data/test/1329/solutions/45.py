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
    d = defaultdict(int)

    def primes(n):
        if n == 1:
            return []
        else:
            tbl = [True] * (n + 1)
            pri = [2]
            for i in range(2, n + 1, 2):
                tbl[i] = False
            k = 3
            while k <= n:
                if tbl[k]:
                    pri.append(k)
                    for i in range(k, n + 1, k):
                        tbl[i] = False
                k += 2
            return pri
    p = primes(n)
    for i in range(2, n + 1):
        ii = i
        for j in p:
            while True:
                if ii % j == 0:
                    d[j] += 1
                    ii //= j
                else:
                    break
            if ii == 1:
                break
    d2 = 0
    d4 = 0
    d14 = 0
    d24 = 0
    d74 = 0
    for i in list(d.values()):
        if i >= 2:
            d2 += 1
            if i >= 4:
                d4 += 1
                if i >= 14:
                    d14 += 1
                    if i >= 24:
                        d24 += 1
                        if i >= 74:
                            d74 += 1

    print((d4 * (d4 - 1) * (d2 - 2) // 2 + d14 * (d4 - 1) + d24 * (d2 - 1) + d74))

    return None


def __starting_point():
    main()


__starting_point()
