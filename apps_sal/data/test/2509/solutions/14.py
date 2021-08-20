(N, K) = map(int, input().split())
ans = 0
for b in range(1, N + 1):
    if b <= K:
        continue
    ans += (N + 1) // b * (b - K)
    ans += max((N + 1) % b - K, 0)
    if K == 0:
        ans -= 1
print(ans)
