import numpy as np
(N, M, X) = map(int, input().split())
C = []
A = []
for _ in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(np.array(l[1:]))
ans = 10 ** 100
for i in range(2 ** N):
    rikaido = np.zeros(M)
    c = 0
    for j in range(N):
        if i >> j & 1:
            c += C[j]
            rikaido += A[j]
    if all([x >= X for x in rikaido]):
        ans = min(ans, c)
print(ans if ans != 10 ** 100 else -1)
