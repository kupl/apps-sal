def find_ans(N, K):
    if K == 0:
        return N**2

    else:
        ans = 0
        for i in range(K + 1, N + 1):
            ans += (N // i) * (i - K) + max(N % i - (K - 1), 0)

        return ans


N, K = list(map(int, input().split()))
print((find_ans(N, K)))
