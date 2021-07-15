#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    cnt = Counter(A)
    if len(cnt) != 2:
        print("NO")
        return

    ps = list(cnt.items())
    if ps[0][1] != ps[1][1]:
        print("NO")
        return

    print("YES")
    print(ps[0][0], ps[1][0])

def __starting_point(): main()

__starting_point()
