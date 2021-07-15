import numpy as np
n,k = list(map(int,input().split()))

A = np.array(input().split(),np.int)

F = np.array(input().split(),np.int)


A.sort()
F.sort()

F_ = F[::-1]

left = -1
right = (A * F_).sum()

while (right - left) > 1:
    s = (left + right) // 2
    r = np.maximum(0, A - s // F_).sum() <= k
    if r:
        right = s 
    else:
        left = s 

print(right)

