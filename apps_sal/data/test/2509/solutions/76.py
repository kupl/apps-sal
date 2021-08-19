def find_ans(N, K):
    # K==0ならN^2が答え
    if K == 0:
        return N**2

    # そうでなければK+1～Nについて一般式
    else:
        ans = 0
        for i in range(K + 1, N + 1):
            ans += (N // i) * (i - K) + max(N % i - (K - 1), 0)

        return ans


N, K = list(map(int, input().split()))
print((find_ans(N, K)))
