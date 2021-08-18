import sys
import numpy as np
from math import factorial


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, A, B = lr()
V = np.array(lr())
V.sort()
ave = V[-A:].sum() / A
print(ave)
border = V[-A]
left_i = np.searchsorted(V, border, side='left')
right_i = np.searchsorted(V, border, side='right')
seg = right_i - left_i
done = N - right_i
use = A - done


def combinations_count(n, r):
    return factorial(n) // factorial(n - r) // factorial(r)


answer = combinations_count(seg, use)
if border == ave:
    for x in range(use + 1, min(B - done, seg) + 1):
        answer += combinations_count(seg, x)

print(answer)
