"""
import bisect
from itertools import accumulate
|    author: mr.math - Hakimov Rahimjon     |
|    e-mail: mr.math0777@gmail.com          |
|    created: 10.03.2018 22:24              |
"""
TN = 1


def solution():
    n = int(input())
    v = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ns = [0] * n
    lo = [0] * n
    tt = list(accumulate(t))
    for i in range(n):
        dd = v[i]
        a = 0
        if i != 0:
            dd += tt[i - 1]
            a = tt[i - 1]
        ns[i] += 1
        k = bisect.bisect_right(tt, dd)
        if k < n:
            ns[k] -= 1
            lo[k] += v[i] + a
            if k != 0:
                lo[k] -= tt[k - 1]
    ns = list(accumulate(ns))
    for i in range(n):
        lo[i] += t[i] * ns[i]
    print(' '.join(list(map(str, lo))))


while TN != 0:
    solution()
    TN -= 1
