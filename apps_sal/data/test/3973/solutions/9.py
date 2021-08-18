"""
a(x-p) + b (p <= x <= q) の2階階差をとり、imos配列に加える
復元はaccumulateでやる
"""
from itertools import accumulate as acc
import sys


def kaisa2_of_tousa(a, b, p, q, imos, n):
    if p > q:
        return
    imos[p] += b
    if p + 1 < n:
        imos[p + 1] += a - b
    y = a * (q - p) + b
    if q + 1 < n:
        imos[q + 1] += -y - a
    if q + 2 < n:
        imos[q + 2] += y


read = sys.stdin.read
readline = sys.stdin.readline

n, m, *a = list(map(int, read().split()))

imos = [0] * (2 * m + 1)
ans = 0
for p, q in zip(a, a[1:]):
    if p > q:
        q += m
    ans += q - p
    kaisa2_of_tousa(-1, 0, p + 1, q, imos, 2 * m + 1)

res = list(acc(acc(imos)))


v = 0
for i in range(1, m + 1):
    w = res[i] + res[i + m]
    v = min(v, w)

print((ans + v))
