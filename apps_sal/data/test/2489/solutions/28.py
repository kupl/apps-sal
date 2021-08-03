#!/usr/bin/env python3
import sys
import collections

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(MI())


N = I()
A = LI()
A.sort()
cnt = collections.Counter(A)
MAX = A[-1] + 1
# end = A[-1] ** 0.5

for a in A:
    if cnt[a] >= 2:
        del cnt[a]
    for i in range(a * 2, MAX, a):
        del cnt[i]

print((sum(cnt.values())))
