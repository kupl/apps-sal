# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

M, K = lr()
if K >= 2 ** M:
    print((-1)); return
if M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print((-1))
    return
A = [x for x in range(2 ** M) if x != K]
answer = A + [K] + A[::-1] + [K]
print((*answer))
# 22

