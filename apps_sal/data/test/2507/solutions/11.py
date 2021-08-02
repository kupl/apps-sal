import numpy as np
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort()


a = np.array(a)
f = np.array(f)
f_ = f[::-1]

left = -1
right = np.max(a * f_)

while left + 1 < right:
    mid = (left + right) // 2
    x = np.maximum(0, a - (mid // f_)).sum() <= k
    if x:
        right = mid
    else:
        left = mid

print(right)
