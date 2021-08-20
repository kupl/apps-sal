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

    def construct_sum(segtree, a, n):
        for i in range(n):
            segtree[n + i] = a[i]
        k = math.ceil(math.log2(n)) % 2
        for i in range(n - 1, 0, -1):
            if math.ceil(math.log2(i + 1)) % 2 == k:
                segtree[i] = segtree[2 * i] | segtree[2 * i + 1]
            else:
                segtree[i] = segtree[2 * i] ^ segtree[2 * i + 1]

    def update_sum(pos, x, n):
        pos += n - 1
        segtree[pos] = x
        k = math.ceil(math.log2(n)) % 2
        while pos > 1:
            pos >>= 1
            if math.ceil(math.log2(pos + 1)) % 2 == k:
                segtree[pos] = segtree[2 * pos] | segtree[2 * pos + 1]
            else:
                segtree[pos] = segtree[2 * pos] ^ segtree[2 * pos + 1]
    (n, m) = mdata()
    a = mdata()
    segtree = [0] * (2 * len(a))
    construct_sum(segtree, a, len(a))
    for i in range(m):
        (p, b) = mdata()
        update_sum(p, b, len(a))
        print(segtree[1])


def __starting_point():
    main()


__starting_point()
