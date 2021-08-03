N, K = map(int, input().split())
ans = 0
if K == 0:
    print(N * N)
    return
else:
    for i in range(K + 1, N + 1):
        ans = ans + (N // i) * max(0, i - K) + max(0, N % i - K + 1)
    print(ans)
