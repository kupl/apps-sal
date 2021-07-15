N, K = map(int, input().split())
ans = 0
for b in range(1, N+1):
    ans += max(0, b - K) * (N // b)
    ans += max(0, N % b + 1 - K)
    if K == 0:
        ans -= 1
print(ans)
