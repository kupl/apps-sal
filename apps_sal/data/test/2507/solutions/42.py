import numpy as np
N, K = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.int64)
F = np.array(input().split(), dtype=np.int64)
A = np.sort(A)
F = np.sort(F)[::-1]


def C(x):
    train = np.maximum(0, A - x // F).sum()
    return train <= K


left = -1
right = 10 ** 12 + 1
while right > left + 1:
    mid = (right + left) // 2
    if C(mid):  # 食べきれる場合
        right = mid
    else:
        left = mid

ans = right
print(ans)


