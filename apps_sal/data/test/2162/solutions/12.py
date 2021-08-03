def main():
    k1, k2, k3 = map(int, input().split())
    n = k1 + k2 + k3
    arr = [0 for _ in range(n)]
    a = list(map(int, input().split()))
    for i in a:
        arr[i - 1] = 1
    a = list(map(int, input().split()))
    for i in a:
        arr[i - 1] = 2
    a = list(map(int, input().split()))
    for i in a:
        arr[i - 1] = 3
    dp = [0, 0, 0]
    for i in arr:
        if i == 1:
            dp[1] += 1
            dp[2] += 1
        if i == 2:
            dp[1] = min(dp[0], dp[1])
            dp[0] += 1
            dp[2] += 1
        if i == 3:
            dp[2] = min(dp[0], dp[1], dp[2])
            dp[0] += 1
            dp[1] += 1
    print(min(dp))


def __starting_point():
    main()


__starting_point()
