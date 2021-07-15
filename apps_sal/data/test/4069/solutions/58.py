import sys

X, K, D = list(map(int, input().split()))
X = abs(X)

c = min(K, X // D)
K -= c
X -= D * c
if K % 2 == 0:
    print(X)
else:
    print((abs(X - D)))

