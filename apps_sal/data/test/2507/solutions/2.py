import numpy as np

N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))  # consumption coefficient of members
F = list(map(int, input().split(" ")))  # difficulty of food

# pair fastest eaters (low consumption coefficient) with most difficult foods
A.sort()
F.sort(reverse=True)
A = np.array(A)
F = np.array(F)

maxT = np.max(A * F)
# use binary search to find lowest possible T
left = -1
right = maxT
while left + 1 < right:
    mid = (left + right) // 2
    if np.maximum(0, A - (mid // F)).sum() <= K:
        right = mid
    else:
        left = mid
print(right)
