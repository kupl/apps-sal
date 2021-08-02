import sys
from math import ceil, floor, factorial
import operator as op
from functools import reduce

input = sys.stdin.readline


def ncr(n, r):
    f = factorial
    return (f(n) // f(r) // f(n - r)) % 998244353


n, m, k = map(int, input().split())

if k >= n:
    print(0)
    return

colorings = m
for i in range(k):
    colorings *= (m - 1)
    colorings %= 998244353

print(int(((ncr(n - 1, k) % 998244353) * colorings) % 998244353) % 998244353)
