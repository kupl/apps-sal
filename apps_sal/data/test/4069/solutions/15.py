(X, K, D) = list(map(int, input().split()))
X = abs(X)
c = min(K, X // D)
K -= c
X -= D * c
if K == 0:
    print(X)
elif K % 2:
    print(abs(X - D))
else:
    print(X)
