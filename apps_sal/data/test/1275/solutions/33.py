(N, K) = map(int, input().split())
ans = 0
for AB in range(max(2, K + 2), min(2 * N, K + 2 * N) + 1):
    ans += (min(AB - 1, N) - max(1, AB - N) + 1) * (min(AB - K - 1, N) - max(1, AB - K - N) + 1)
print(ans)
