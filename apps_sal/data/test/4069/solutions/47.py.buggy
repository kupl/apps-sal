import sys
X, K, D = map(int, input().split())
X = abs(X)
if X // D >= K:
    print(X - K * D)
    return
K = K - (X // D)
A = X - X // D * D
if K % 2 == 0:
    print(A)
else:
    print(abs(A - D))
