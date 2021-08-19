import os
import os
import sys
from functools import reduce
from operator import xor
import numpy as np
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
IINF = 10 ** 18
MOD = 10 ** 9 + 7
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = np.array(A, dtype=np.int64)


def dump(arr):
    for a in arr:
        print(np.binary_repr(a, 60))
    print()


odds = reduce(xor, A)
ans = odds
A &= ~odds
rank = 0
for d in reversed(list(range(60))):
    bits1 = (A >> d & 1).astype(bool)
    pos = bits1[rank:].argmax() + rank
    if not bits1[pos]:
        continue
    if pos < rank:
        continue
    pivot_row = A[pos]
    A[bits1] ^= pivot_row
    A[pos] = pivot_row
    (A[pos], A[rank]) = (A[rank], A[pos])
    rank += 1
ans += reduce(xor, A) * 2
print(ans)
