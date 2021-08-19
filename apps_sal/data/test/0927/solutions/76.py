def main():
    (n, m, *a) = list(map(int, open(0).read().split()))
    t = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    a.sort(reverse=True)
    b = [t[i] for i in a]
    dp = [-float('Inf')] * (n + 10)
    dp[0] = 0
    for i in range(2, n + 1):
        dp[i] = max((dp[i - j] + 1 for j in b))
    nums = []
    for i in range(dp[n], 0, -1):
        for x in a:
            if dp[n - t[x]] == i - 1:
                nums.append(x)
                n -= t[x]
                break
    ans = ''.join(map(str, nums))
    print(ans)


def __starting_point():
    main()


__starting_point()
