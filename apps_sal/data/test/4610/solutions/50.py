N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

X = [0] * N

for i in range(N):
    X[A[i] - 1] += 1

X = sorted(X, reverse=True)

S = sum(X[:K])

ans = N - S

print(ans)
