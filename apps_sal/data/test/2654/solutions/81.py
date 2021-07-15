#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


n = I()
ab = list(map(int, sys.stdin.read().split()))
a = ab[::2]
b = ab[1::2]
a.sort()
b.sort()

if n % 2 == 0:
    m1 = (a[n // 2 - 1] + a[n // 2]) / 2
    m2 = (b[n // 2 - 1] + b[n // 2]) / 2
    print((int((m2 - m1) * 2 + 1)))
else:
    m1 = a[n // 2]
    m2 = b[n // 2]
    print((m2 - m1 + 1))

