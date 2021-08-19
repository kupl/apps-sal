import numpy as np
K = int(input())

N = 50
num = K // N
r = K % N
L = [N - 1] * N
L = np.array(L)
L += num
for i in range(N):
    if i < r:
        L[i] += N - (r - 1)
    else:
        L[i] -= r

print(N)
print((*L))
