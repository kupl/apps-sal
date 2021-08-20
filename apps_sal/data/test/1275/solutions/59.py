(N, K) = list(map(int, input().split()))
ans = 0
for i in range(2, 2 * N + 1):
    ab = min(i - 1, 2 * N - i + 1)
    cd = min(i - K - 1, 2 * N - i + K + 1)
    if 1 <= ab <= N and 1 <= cd <= N:
        ans += ab * cd
print(ans)
