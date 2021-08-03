import sys
import numpy as np
N, K = map(int, input().split())
A = np.array([int(i) for i in input().split()])
F = np.array([int(i) for i in input().split()])
A = np.sort(A)
F = np.sort(F)[::-1]

Asum = A.sum()


def test(x):
    return Asum - np.minimum(A, x // F).sum() <= K


l = 0
r = 10**18 * 2 + 1
while r - l > 1:
    # print(l,r)
    m = (l + r) // 2
    if test(m):
        r = m
    else:
        l = m
if test(l):
    print(l)
else:
    print(l + 1)
