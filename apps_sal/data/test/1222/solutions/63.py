def is_good(mid, key):
    S = list(map(int, str(mid)))
    N = len(S)
    dp = [[[0] * 11 for _ in range(2)] for _ in range(N + 1)]
    dp[1][1][10] = 1
    for k in range(1, S[0]):
        dp[1][1][k] = 1
    dp[1][0][S[0]] = 1
    for i in range(1, N):
        for k in range(1, 11):
            dp[i + 1][1][k] += dp[i][0][10] + dp[i][1][10]
        for is_less in range(2):
            for k in range(10):
                for l in range(k - 1, k + 2):
                    if not 0 <= l <= 9 or (not is_less and l > S[i]):
                        continue
                    dp[i + 1][is_less or l < S[i]][l] += dp[i][is_less][k]
    return sum(dp[N][0][k] + dp[N][1][k] for k in range(10)) >= key


def binary_search(bad, good, key):
    while good - bad > 1:
        mid = (bad + good) // 2
        if is_good(mid, key):
            good = mid
        else:
            bad = mid
    return good


K = int(input())
print((binary_search(0, 3234566667, K)))

