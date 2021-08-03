import numpy as np

N, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())), reverse=True)

A = np.array(A, np.int64)
F = np.array(F, np.int64)

Asum = sum(A)


def test(X):
    return (Asum - np.minimum(A, X // F).sum() <= K)


l = -1
r = 10**12

while (l + 1 < r):
    mid = (l + r) // 2
    if test(mid):
        r = mid
    else:
        l = mid

ans = r
print(ans)
