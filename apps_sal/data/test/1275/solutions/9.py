N, K = map(int, input().split())

l = max(2, 2 + K)
r = min(2 * N, 2 * N + K)

ans = 0
for i in range(l, r + 1):
    la = max(1, i - N)
    ra = min(i - 1, N)
    lc = max(i - K - N, 1)
    rc = min(i - K - 1, N)
    ans += (ra - la + 1) * (rc - lc + 1)

print(ans)
