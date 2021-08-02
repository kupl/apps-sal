#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import bisect
from collections import Counter

read_int = lambda: int(sys.stdin.readline())
read_ints = lambda: list(map(int, sys.stdin.readline().split()))
read_int_list = lambda: list(read_ints())
read = lambda: sys.stdin.readline().strip()
read_list = lambda: sys.stdin.readline().split()


def main():
    n, k = read_ints()
    s = read()
    d = Counter(s)
    res = k * min(d.values()) if len(d) == k else 0
    print(res)


main()
