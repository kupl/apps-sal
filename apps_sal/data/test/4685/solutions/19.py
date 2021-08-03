X = list(map(int, input().split()))
K = int(input())
X.sort()
for i in range(K):
    X[-1] = X[-1] * 2
print(sum(X))
