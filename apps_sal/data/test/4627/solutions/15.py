import sys
import math
import os
from io import BytesIO, IOBase
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1000000000.0) + 7


def main():
    for t in range(int(data())):
        n = int(data())
        a = mdata()
        e = 0
        for i in range(n):
            if a[i] % 2 == 0:
                e += 1
        if e % 2 == 0:
            out('YES')
        else:
            s = set(a)
            flag = False
            for i in a:
                if i + 1 in s:
                    flag = True
                    break
            if flag == True:
                out('YES')
            else:
                out('NO')


def __starting_point():
    main()


__starting_point()
