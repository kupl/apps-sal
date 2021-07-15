import sys
X, K, D = map(int, input().split())
if K * D < abs(X):
    print(abs(X) - K * D)
    return

tmp = X//D
X -= tmp * D
K -= tmp
if K%2 == 0:
    print(abs(X)%D)
else:
    print(abs(X-D))
