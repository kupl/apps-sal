"""
https://atcoder.jp/contests/abc063/submissions/5538114
"""

from numpy import ceil, array, sum
import sys


def input():
    return sys.stdin.readline().strip()


def is_ok(m):
    tmp = h - m * B
    tmp[tmp < 0] = 0

    if ceil(tmp / (A - B)).sum() > m:
        return False
    return True


N, A, B = map(int, input().split())
h = array(list(int(input()) for _ in range(N)))

r = 10**9
l = 0

while abs(l - r) > 1:

    m = (r + l) // 2

    if is_ok(m):
        r = m
    else:
        l = m

print(r)
