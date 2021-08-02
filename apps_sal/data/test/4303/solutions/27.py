N, K = map(int, input().split())
X = list(map(int, input().split()))
T = 10**18
for i in range(N - K + 1):
    if X[i + K - 1] <= 0:
        T = min(T, -X[i])
    elif X[i] >= 0:
        T = min(T, X[i + K - 1])
    else:
        T = min(T, X[i + K - 1] - X[i] + min(-X[i], X[i + K - 1]))
print(T)
