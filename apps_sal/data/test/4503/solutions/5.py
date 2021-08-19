import numpy as np
(H, N) = map(int, input().split())
A = np.array(list(map(int, input().split())))
if H <= np.sum(A):
    print('Yes')
else:
    print('No')
