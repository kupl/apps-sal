import sys
import math
import itertools as it
import operator as op
(n, c) = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))
tl = tr = sl = sr = 0
for i in range(n):
    tl += T[i]
    tr += T[n - 1 - i]
    sl += max(0, P[i] - c * tl)
    sr += max(0, P[n - 1 - i] - c * tr)
if sl > sr:
    print('Limak')
elif sl == sr:
    print('Tie')
else:
    print('Radewoosh')
