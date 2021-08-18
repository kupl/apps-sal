def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    required = [None] + [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [0 for _ in range(max(10, N + 1))]
    candidates = {}
    for a in A:
        req = required[a]
        if dp[req] < a:
            dp[req] = a
            candidates[req] = a
    for i in range(N + 1):
        for n_match, num in candidates.items():
            if i - n_match >= 0 and dp[i - n_match] != 0:
                dp[i] = max(dp[i], dp[i - n_match] * 10 + num)
    print(dp[N])


if '__main__' == __name__:
    resolve()
