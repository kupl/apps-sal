import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 二分探索、浮き沈みの沈みに注意
N, K = lr()
A = np.array(lr()); A.sort()
F = np.array(lr()); F.sort(); F = F[::-1]

def check(x):
    cost = np.maximum(0, A - (x // F)).sum()
    return cost <= K

ok = 10 ** 15; ng = -1
while abs(ng-ok) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)

