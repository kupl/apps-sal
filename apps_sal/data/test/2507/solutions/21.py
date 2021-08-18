import numpy as np
N, K = map(int, input().split())


A = np.array(input().split(), np.int64)
B = np.array(input().split(), np.int64)

A.sort()
B.sort()
B = B[::-1]

right = max(A * B)
left = -1


def test(t):

    C = A - t // B
    D = np.where(C < 0, 0, C)
    return D.sum() <= K


while left + 1 < right:
    mid = (left + right) // 2
    if test(mid):
        right = mid
    else:
        left = mid

print(right)
