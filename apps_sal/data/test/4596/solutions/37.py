import numpy as np
n = int(input())
A = np.array(input().split(), np.int64)

cnt = 0
while np.all(A % 2 == 0):
    A = A // 2
    cnt += 1
print(cnt)

