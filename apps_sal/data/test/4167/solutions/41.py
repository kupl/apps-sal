N, K = map(int, input().split())
ans = 0
for r in range(K):
    n = (N + K - r) // K
    if r == 0:
        n -= 1
    if r * 2 % K == 0:
        ans += n ** 3
print(ans)
