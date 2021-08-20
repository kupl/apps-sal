from collections import defaultdict
from bisect import bisect
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(lambda: 0)
for i in range(N):
    d[A[i]] += 1
C = [0] * (N + 1)
for i in d:
    C[d[i]] += 1
C1 = [0] * (N + 1)
C2 = [0] * (N + 1)
for i in range(N):
    C1[i + 1] = C1[i] + (i + 1) * C[i + 1]
    C2[i + 1] = C2[i] + C[i + 1]
l = [0] * N
for n in range(N):
    l[n] = C1[n + 1] // (n + 1) + C2[N] - C2[n + 1]
    l[n] *= -1
for i in range(N):
    print(bisect(l, -(i + 1)))
