import numpy as np


def solve(n, k, a, f):
    a = sorted(a)
    f = sorted(f)[::-1]
    a = np.asarray(a, dtype=int)
    f = np.asarray(f, dtype=int)
    total = np.sum(a)
    l = -1
    r = np.max(a * f)
    while r - l > 1:
        th = (l + r) // 2
        cost = total - np.minimum(a, th // f).sum()
        if cost <= k:
            r = th
        else:
            l = th
    return r


n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
print(solve(n, k, a, f))
