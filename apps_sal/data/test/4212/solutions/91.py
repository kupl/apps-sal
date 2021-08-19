from sys import stdin
import itertools
(N, M, Q) = [int(x) for x in stdin.readline().rstrip().split()]
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    (a[i], b[i], c[i], d[i]) = [int(x) for x in stdin.readline().rstrip().split()]
    a[i] -= 1
    b[i] -= 1
ans = 0
for A in itertools.combinations_with_replacement(list(range(1, M + 1)), N):
    cur = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            cur += d[i]
    if ans < cur:
        ans = cur
print(ans)
