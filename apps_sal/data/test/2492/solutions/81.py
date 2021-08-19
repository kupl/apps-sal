import numpy as np

N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
A.sort()
posi = A[A > 0]
zero = A[A == 0]
nega = A[A < 0]

# 積がx以下の組を求める


def check(x):
    count = 0  # 積がx以下の組
    if x >= 0:
        count += len(zero) * N  # zero * N
    count += np.searchsorted(A, x // posi, side='right').sum()  # posi * N
    count += (N - np.searchsorted(A, (-x - 1) // (-nega), side='right')).sum()  # nega * N
    count -= np.count_nonzero(A * A <= x)  # 自分自身との組
    return count // 2  # 重複を消す


# 二分探索
low = -10 ** 18
high = 10 ** 18
while low + 1 < high:
    mid = (low + high) // 2
    if check(mid) < K:  # OK
        low = mid
    else:               # NG
        high = mid

print(high)
