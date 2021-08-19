(N, K) = map(int, input().split())
ans = max(0, (N - K + 1) / N)
for dice in range(1, min(N, K - 1) + 1):
    for time in range(1, len(bin(K)) + 2):
        dice *= 2
        if dice >= K:
            ans += 1 / (N * 2 ** time)
            break
print(ans)
