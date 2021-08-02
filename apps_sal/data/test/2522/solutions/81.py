import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

l, r = 0, N + 1
while r - l > 1:
    m = (r + l) // 2
    if np.all(B[N - m:] > A[:m]):
        l = m
    else:
        r = m

if np.all(B[:N - l] < A[l:]):
    print('Yes')
    print((*np.roll(B, l)))
else:
    print('No')
