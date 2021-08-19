(N, K) = list(map(int, input().split()))
ans = 0
for i in range(2, 2 * N + 1):
    j = i - K
    if not 2 <= j <= 2 * N:
        continue
    ans += min(i - 1, 2 * N - i + 1) * min(j - 1, 2 * N - j + 1)
print(ans)
