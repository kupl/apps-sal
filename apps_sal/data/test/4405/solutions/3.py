

from bisect import bisect_left, bisect_right
from collections import Counter as C

n_ = int(input())
l = sorted(C(map(int, input().split())).values())
n = len(l)
i = res = 0


def f(x):
    i = 0
    for m in range(33):
        t = x << m
        i = bisect_left(l, t, i)
        if i == n:
            return t - x
        i += 1


res = 0
for x in range(1, n_ + 1):
    res = max(res, f(x))

print(res)
