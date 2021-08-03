N, K = map(int, input().split())
ans = 0
if K == 0:
    print(N**2)
else:
    for i in range(K + 1, N + 1):
        ans += (N // i) * (i - K)
        if (N % i) - K + 1 > 0:
            ans += (N % i) - K + 1
    print(ans)
