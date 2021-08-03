N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))
X = M * N - sum(A)

if X <= K and X >= 0:
    print(X)
elif X <= K and X < 0:
    print("0")
else:
    print("-1")
