import numpy as np

N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
A.sort()
posi = A[A > 0]
zero = A[A == 0]
nega = A[A < 0]


def check(x):
    count = 0
    if x >= 0:
        count += len(zero) * N
    count += np.searchsorted(A, x // posi, side='right').sum()
    count += (N - np.searchsorted(A, (-x - 1) // (-nega), side='right')).sum()
    count -= np.count_nonzero(A * A <= x)
    return count // 2


low = -10 ** 18
high = 10 ** 18
while low + 1 < high:
    mid = (low + high) // 2
    if check(mid) < K:
        low = mid
    else:
        high = mid

print(high)
