import numpy as np
(n, k, q) = list(map(int, input().split()))
A = [k for _ in range(n)]
for i in range(q):
    t = int(input())
    A[t - 1] += 1
for i in range(n):
    if A[i] - q > 0:
        print('Yes')
    else:
        print('No')
