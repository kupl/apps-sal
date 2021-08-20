import numpy as np
(N, A, B) = map(int, input().split())
h = np.sort([int(input()) for i in range(N)])


def enough(A, B, h, T):
    h = np.ceil((h - B * T) / (A - B))
    count = sum(h[h > 0])
    return True if count <= T else False


right = 10 ** 9
left = 1
while right != left:
    mid = (left + right) // 2
    if enough(A, B, h, mid):
        right = mid
    else:
        left = mid + 1
print(left)
