import math
import numpy as np

n, k = list(map(int, input().split()))
a = np.array(input().split(), dtype=int)
f = np.array(input().split(), dtype=int)

a = np.sort(a)[::-1]
f = np.sort(f)

ok = 10**18
ng = -1


def isOK(val, arr, farr, k):
    return arr.sum() - np.minimum(arr, val // farr).sum() <= k


while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if isOK(mid, a, f, k):
        ok = mid
    else:
        ng = mid

print(ok)
