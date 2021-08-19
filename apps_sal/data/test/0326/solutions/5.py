"""
自宅用PCでの解答
"""
import math
import itertools
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
alp = 'abcdefghijklmnopqrstuvwxyz'
INF = 1 << 32 - 1


def main():
    n = int(ipt())
    wrds = []
    hq = []
    usd = set()
    for i in range(n):
        (s, c) = input().split()
        c = int(c)
        wrds.append((s, c))
        hpq.heappush(hq, (c, s, 1))
    while hq:
        (hc, hs, hp) = hpq.heappop(hq)
        usd.add((hs, hp))
        ls = len(hs)
        if hs == hs[::-1]:
            print(hc)
            return
        for (si, ci) in wrds:
            lsi = len(si)
            if lsi > ls:
                if hp == 1:
                    wt = si[::-1]
                    if hs == wt[:ls] and (not (wt[ls:], -1) in usd):
                        hpq.heappush(hq, (hc + ci, wt[ls:], -1))
                elif hs == si[:ls] and (not (si[ls:], 1) in usd):
                    hpq.heappush(hq, (hc + ci, si[ls:], 1))
            elif hp == 1:
                wt = si[::-1]
                if wt == hs[:lsi] and (not (hs[lsi:], 1) in usd):
                    hpq.heappush(hq, (hc + ci, hs[lsi:], 1))
            elif si == hs[:lsi] and (not (hs[lsi:], -1) in usd):
                hpq.heappush(hq, (hc + ci, hs[lsi:], -1))
    print(-1)
    return None


def __starting_point():
    main()


__starting_point()
