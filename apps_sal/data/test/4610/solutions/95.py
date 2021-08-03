N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
X = [0 for _ in range(N + 1)]
for a in A:
    X[a] += 1
X.sort(reverse=True)
print((N - sum(X[0:K])))
