import sys
#import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


# 最小値と最大値の絶対値がどちらが大きいか
N = ir()
A = lr()
if abs(max(A)) >= abs(min(A)):
    i = A.index(max(A))
    print((2 * (N - 1)))
    print((i + 1, 2))
    print((i + 1, 2))
    for i in range(2, N):
        print((i, i + 1))
        print((i, i + 1))
else:
    i = A.index(min(A))
    print((2 * (N - 1)))
    print((i + 1, N - 1))
    print((i + 1, N - 1))
    for i in range(2, N):
        print((N - i + 1, N - i))
        print((N - i + 1, N - i))

# 50
