from collections import Counter
from itertools import accumulate
n = int(input())
A = tuple(map(int, input().split()))
C = Counter(A)
D = [0] * (n + 1)
for v in C.values():
    D[v] += 1
E = tuple(accumulate((k * d for (k, d) in enumerate(D))))
D = tuple(accumulate(D))
F = [0] * (n + 1)
for x in range(1, n + 1):
    temp = (E[x] + x * (D[n] - D[x])) // x
    F[x] = temp
for k in range(1, n + 1):
    ok = 0
    ng = n + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if k <= F[mid]:
            ok = mid
        else:
            ng = mid
    print(ok)
