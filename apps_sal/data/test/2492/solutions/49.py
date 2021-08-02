from numpy import *
N, K = map(int, input().split())
A = array(sorted(list(map(int, input().split()))))
nega = A[A < 0]
zera = A[A == 0]
posa = A[0 < A]


def cnt(x):
    y = 0
    if x >= 0:
        y += N * len(zera)
    y += searchsorted(A, x // posa, side="right").sum()
    y += N * len(nega) - searchsorted(A, -(-x // nega)).sum()
    y -= len(A[A * A <= x])
    return y // 2


r = 10**18
l = -r - 1

while r - l > 1:
    c = (r + l) // 2
    if K <= cnt(c):
        r = c
    else:
        l = c

print(r)
