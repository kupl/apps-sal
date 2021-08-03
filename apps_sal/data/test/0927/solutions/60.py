def main():
    C = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = [0] + [-1] * N
    K = {a: C[a - 1] for a in A}

    for i in range(min(K.values()), N + 1):
        try:
            dp[i] = max(dp[i - v] * 10 + k for k, v in list(K.items()) if i - v >= 0 and dp[i - v] >= 0)
        except ValueError:
            dp[i] = -1
    print((dp[N]))


main()
