#!/usr/bin/env python3
import sys
import numpy as np

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(MI())


S = ST()

cnt = np.zeros(2019)
cnt[0] = 1
res = 0
tmp = 1
for s in S[::-1]:
    res += int(s) * tmp
    res %= 2019
    cnt[res] += 1
    tmp *= 10
    tmp %= 2019

ans = 0
for c in cnt[cnt >= 2]:
    ans += c * (c - 1) // 2

print((int(ans)))

