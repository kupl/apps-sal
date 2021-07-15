import numpy as np
def bin_search(left, right, check):
    while left + 1 < right:
        middle = (left + right) >> 1
        if check(middle):
            right = middle
        else:
            left = middle
    return right

def check(m):
    return np.maximum(A - m // F, Z).sum() <= K

N, K = map(int, input().split())
A = np.array(input().split(), dtype=np.int32)
F = np.array(input().split(), dtype=np.int32)
Z = np.zeros((N,), dtype=np.int32)
A.sort()
F = F[np.argsort(-F)]

print(bin_search(-1, 10 ** 12, check))
