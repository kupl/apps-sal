import sys
import math
import os
from io import BytesIO, IOBase
from bisect import bisect_left as bl, bisect_right as br, insort
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9) + 7


def main():

    for i in range(int(data())):
        n = int(data())
        A = mdata()
        cnt1 = 1
        cnt2 = 1
        A.sort()
        for i in range(n):
            if A[i] <= cnt2:
                cnt2 += 1
                cnt1 = cnt2
            else:
                cnt2 += 1
        out(cnt1)


def __starting_point():
    main()


__starting_point()
