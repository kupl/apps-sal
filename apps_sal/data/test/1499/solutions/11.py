import sys
import math
import itertools as it
import operator as op
import fractions as fr


n, m = list(map(int, sys.stdin.readline().split()))

A = [[-1 for _ in range(4)] for _ in range(n)]

i, j = 0, 0
for k in range(1, m + 1):
    A[i][j] = k
    if i == n - 1 and j == 3:
        i, j = 0, 2
    elif j > 1:
        i += 1
    j = [3, 2, 1, 0][j]

i, j = 0, 1
B = []
for _ in range(4 * n):
    if A[i][j] != -1:
        B.append(A[i][j])
    if j == 3:
        i += 1
    j = [2, 0, 3, 1][j]

print(' '.join(map(str, B)))
