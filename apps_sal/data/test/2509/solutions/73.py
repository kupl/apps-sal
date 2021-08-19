(N, K) = map(int, input().split())
ans = 0
for b in range(K + 1, N + 1):
    if b == 1:
        ans += 1
        continue
    ans += N // b * (b - K) + max(N % b - K + 1, 0)
print(ans)
