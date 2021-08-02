#! usr/bin/env python
# -*- coding : utf-8 -*-

from collections import deque
import heapq
import bisect
import math


def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    for i in range(1 << n):
        cur = 0
        for j in range(n):
            if (i >> j) & 1:
                cur += a[j]
            else:
                cur -= a[j]

        if cur % 360 == 0:
            print("YES")
            return

    print("NO")


def __starting_point():
    main()


__starting_point()
