(N, K) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 10 ** 10
for i in range(N - K + 1):
    ans = min(ans, abs(x[i]) + (x[i + K - 1] - x[i]), abs(x[i + K - 1]) + (x[i + K - 1] - x[i]))
print(ans)
