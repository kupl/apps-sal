N = int(input())
K = int(input())
X = 1
for i in range(N):
    if X < K:
        X += X
    else:
        X += K
print(X)
