(N, K) = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    (p, r) = divmod(N, i)
    ans += max(0, i - K) * p + max(0, r - K + 1)
    if K == 0:
        ans -= 1
print(ans)
