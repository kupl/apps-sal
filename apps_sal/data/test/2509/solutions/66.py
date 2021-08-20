(N, K) = list(map(int, input().split()))
ans = 0
if K == 0:
    print(N * N)
else:
    for b in range(K + 1, N + 1):
        x = N // b
        ans += (b - K) * x
        y = N % b
        ans += max(0, y - K + 1)
    print(ans)
