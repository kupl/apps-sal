N, K = map(int, input().split())
ans = 1

for i in range(K, N + 1):
    ans += N * i - i * i + i + 1

print(ans % 1000000007)
