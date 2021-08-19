import sys
from collections import Counter
readline = sys.stdin.readline
(N, M) = map(int, readline().split())
A = list(map(int, readline().split()))
A.sort()
Ans = [None] * N
pre = 0
C = Counter()
for i in range(N):
    a = A[i]
    C[i % M] += a
    Ans[i] = pre + C[i % M]
    pre = Ans[i]
print(*Ans)
