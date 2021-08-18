N, K = map(int, input().split())
high = [int(input()) for _ in range(N)]
s_high = sorted(high)
ans = 10**9
for i in range(N - K + 1):
    j = s_high[i + K - 1] - s_high[i]
    ans = min(ans, j)
print(ans)
