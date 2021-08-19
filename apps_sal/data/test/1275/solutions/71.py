(N, K) = list(map(int, input().split()))
ans = 0
for i in range(2, 2 * N + 1):
    A = i
    B = i - K
    if 2 * N >= B >= 2:
        X = min(N, A - 1) - max(1, A - N) + 1
        Y = min(N, B - 1) - max(1, B - N) + 1
        ans += X * Y
print(ans)
