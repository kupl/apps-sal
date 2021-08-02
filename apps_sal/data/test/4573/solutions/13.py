import numpy as np

N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
x = np.median(X)
index = N // 2
m1 = Y[index]
m2 = Y[index - 1]

for i in range(N):
    if X[i] < x:
        print(m1)
    else:
        print(m2)
