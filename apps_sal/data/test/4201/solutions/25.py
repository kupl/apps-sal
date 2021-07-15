import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
inf = 10**9


def main():
    h, w, k = list(map(int, input().split()))
    c = []

    for i in range(h):
        c.append(list(input()))

    # print(c)

    r = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            bh = list(str(bin(i))[2:].zfill(h))
            bw = list(str(bin(j))[2:].zfill(w))
            # print(bh, bw)
            count = 0
            for m in range(h):
                for l in range(w):
                    if bh[m] == '1' and bw[l] == '1' and c[m-1][l-1] == '#':
                        count += 1
            # print(count)
            if count == k:
                r += 1

    print(r)


def __starting_point():
    main()

__starting_point()
