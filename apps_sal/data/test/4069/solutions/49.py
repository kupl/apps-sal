import sys
(X, K, D) = list(map(int, input().split()))
X = abs(X)
if X >= K * D:
    print(X - K * D)
else:
    k = K - X // D
    x = X - D * (X // D)
    if k % 2:
        print(abs(x - D))
    else:
        print(x)
