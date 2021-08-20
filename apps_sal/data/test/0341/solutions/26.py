def main():
    (n, k) = list(map(int, input().split()))
    (r, s, p) = list(map(int, input().split()))
    t = input()
    dp = [0] * n
    hnd = [0] * n
    point = {'r': p, 's': r, 'p': s}
    h = {'r': 'p', 's': 'r', 'p': 's'}
    dp[0] = point[t[0]]
    hnd[0] = h[t[0]]
    for i in range(1, k):
        dp[i] = dp[i - 1] + point[t[i]]
        hnd[i] = h[t[i]]
    for i in range(k, n):
        if hnd[i - k] != h[t[i]]:
            hnd[i] = h[t[i]]
            dp[i] += dp[i - 1] + point[t[i]]
        else:
            dp[i] = dp[i - 1]
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
