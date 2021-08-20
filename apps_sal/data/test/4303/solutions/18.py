(N, K) = list(map(int, input().split()))
X = list(map(int, input().split()))
ans = 10 ** 9
for i in range(N - K + 1):
    if X[i] >= 0:
        ans = min(ans, X[K + i - 1])
    elif X[K + i - 1] <= 0:
        ans = min(ans, -X[i])
    else:
        ans = min(ans, 2 * X[K + i - 1] - X[i], X[K + i - 1] - 2 * X[i])
print(ans)
