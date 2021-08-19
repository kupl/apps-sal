(N, M, K) = list(map(int, input().split()))
m = 998244353
ans = M * pow(M - 1, N - 1, m) % m
alpha = 1
for k in range(1, K + 1):
    alpha = alpha * (N - k) * pow(k, m - 2, m) % m
    ans = (ans + M * alpha * pow(M - 1, N - k - 1, m)) % m
print(ans)
