#!/usr/bin/env python3

from collections import Counter

def solve():
    N, M = list(map(int, input().split()))
    gen = list(map(int, input().split()))

    cnt = Counter(gen)

    total = 0
    for gen1, cnt1 in list(cnt.items()):
        for gen2, cnt2 in list(cnt.items()):
            if gen1 == gen2:
                continue
            total += cnt1 * cnt2
    print(total//2)

def __starting_point():
    solve()

__starting_point()
