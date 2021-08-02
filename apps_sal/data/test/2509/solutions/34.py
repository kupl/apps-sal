N, K = map(int, input().split())
if K == 0:
    print(N**2)
    return

ans = 0
for b in range(1, N + 1):
    ans += N // b * max(0, b - K) + max(0, N % b - K + 1)

print(ans)
