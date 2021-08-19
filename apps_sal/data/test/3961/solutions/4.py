#!/usr/bin/env python3

n = int(input())
jmp = list([x - 1 for x in list(map(int, input().split()))])

cache = {}


def DP(i, j):
    if (i, j) not in cache:
        if i == j:
            cache[i, j] = 0
        elif i + 1 == j:
            cache[i, j] = DP(jmp[i], i) + 2
        else:
            cache[i, j] = sum(DP(k, k + 1) for k in range(i, j))

    return cache[i, j]


print(DP(0, n) % (10**9 + 7))
