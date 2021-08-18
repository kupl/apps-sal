import numpy as np

N, Q = map(int, input().split())
S = input()

X = np.zeros(N + 1, dtype='int64')
tmp = 1
while S.find('AC') >= 0 and tmp < N:
    i = S.find('AC')
    X[tmp + i] += 1
    S = S[i + 2:]
    tmp += i + 2
SUM = X.cumsum()

for _ in range(Q):
    l, r = map(int, input().split())
    print(SUM[r - 1] - SUM[l - 1])
