import numpy as np
N, C = list(map(int, input().split()))

# s~tでc
L = np.zeros((C, 10**5 + 1))

for i in range(N):
    s, t, c = list(map(int, input().split()))
    L[c - 1, s - 1] += 1
    L[c - 1, t] -= 1

L = np.cumsum(L, axis=1)
print((int((L > 0).sum(axis=0).max())))
