(N, K) = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
print(sum(X[0:K]))
