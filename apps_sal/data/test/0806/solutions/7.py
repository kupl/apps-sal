def main():
    (n, l, r) = list(map(int, input().split()))
    m = 10 ** 9 + 7
    sub = r - l + 1
    num = [sub // 3] * 3
    if sub % 3 == 1:
        num[l % 3] += 1
    elif sub % 3 == 2:
        num[l % 3] += 1
        num[(l + 1) % 3] += 1
    dp = [1, 0, 0]
    for _ in range(n):
        temp = [0] * 3
        temp[0] = dp[0] * num[0] + dp[1] * num[2] + dp[2] * num[1]
        temp[1] = dp[0] * num[1] + dp[1] * num[0] + dp[2] * num[2]
        temp[2] = dp[0] * num[2] + dp[1] * num[1] + dp[2] * num[0]
        for i in range(3):
            dp[i] = temp[i] % m
    print(dp[0])


def __starting_point():
    main()


__starting_point()
