import numpy as np

N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
F = list(map(int, input().split(" ")))

A.sort()
F.sort(reverse=True)
A = np.array(A)
F = np.array(F)

maxT = np.max(A * F)
left = -1
right = maxT
while left + 1 < right:
    mid = (left + right) // 2
    if np.maximum(0, A - (mid // F)).sum() <= K:
        right = mid
    else:
        left = mid
print(right)
