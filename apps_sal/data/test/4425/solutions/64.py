(N, K) = map(int, input().split())
ans = 0.0
for i in range(1, N + 1):
    x = 0
    while i * 2 ** x < K:
        x += 1
    ans += 1 / (N * 2 ** x)
print(ans)
