def main():
    n, p = map(int, input().split())
    s = input()
    if p == 2:
        ans = 0
        for i in range(n):
            if int(s[i]) % 2 == 0:
                ans += i + 1
        print(ans)
        return
    if p == 5:
        ans = 0
        for i in range(n):
            if int(s[i]) % 5 == 0:
                ans += i + 1
        print(ans)
        return
    dp = [0 for _ in range(p)]
    dp[0] += 1
    x = 0

    for i in range(n):
        x = (x + int(s[n - 1 - i]) * pow(10, i, p)) % p
        dp[x] += 1
    ans = 0
    for i in range(p):
        ans += (dp[i] * (dp[i] - 1)) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
