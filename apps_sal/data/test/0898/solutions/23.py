N, M = list(map(int, input().split()))
ans = 1
if N == 1:
    print(M)
else:
    for n in range(2, int(M ** 0.5) + 1):
        if M % n == 0 and M / N >= n:
            ans = max(ans, n)
            if M // n * N <= M:
                ans = max(ans, M // n)
    print(ans)
