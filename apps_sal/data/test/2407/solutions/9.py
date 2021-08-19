import sys
from math import ceil
readline = sys.stdin.readline
Q = int(readline())
Ans = [None] * Q
for qu in range(Q):
    (N, r) = list(map(int, readline().split()))
    A = list(map(int, readline().split()))
    A = list(set(A))
    A.sort()
    A = [0] + A
    N = len(A)
    Ans[qu] = min((N - i for i in range(1, N + 1) if A[i - 1] <= r * (N - i)))
print('\n'.join(map(str, Ans)))
