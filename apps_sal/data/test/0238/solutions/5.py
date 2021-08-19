import copy
from itertools import accumulate
import sys
input = sys.stdin.readline
(n, m, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
ANS = 0
for i in range(m):
    B = copy.deepcopy(A)
    for j in range(i, n, m):
        B[j] -= k
    SUM = list(accumulate(B))
    SUMMIN = [float('inf')] * n + [0]
    if i == 0:
        SUMMIN[0] = 0
    for j in range(max(1, i), n):
        if j % m == i % m:
            SUMMIN[j] = min(SUMMIN[j - 1], SUM[j - 1])
        else:
            SUMMIN[j] = SUMMIN[j - 1]
    for j in range(i, n):
        ANS = max(ANS, SUM[j] - SUMMIN[j])
print(ANS)
