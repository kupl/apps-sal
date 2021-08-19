import numpy as np
n = int(input())
A = np.array(list(map(int, input().split())))
minus = np.count_nonzero(A < 0)
A = np.abs(A)
if 0 in A or minus % 2 == 0:
    print(np.sum(A))
else:
    print(np.sum(A) - 2 * np.min(A))
