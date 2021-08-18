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
    s = input()
    ls = len(s)
    t = input()
    if t[0] in s:
        idx = s.find(t[0])
    else:
        print((-1))
        return
    for i in t[1::]:
        nt = s.find(i, idx % ls + 1)
        ntl = s.find(i)
        if ntl == -1:
            print((-1))
            return
        elif nt == -1:
            idx = (idx // ls) * ls + ls + ntl
        else:
            idx = (idx // ls) * ls + nt
    print((idx + 1))
    return None


def __starting_point():
    main()


__starting_point()
