def main():
    n = int(input())

    a = [int(x) for x in input().split()]
    a += a

    s, f = [int(x) for x in input().split()]

    dp = [0 for _ in range(2 * n + 1)]
    for i in range(2 * n):
        dp[i + 1] = dp[i] + a[i]

    ans, sum = 0, 0

    for i in range(n):
        cur_sum = dp[f + n - i - 1] - dp[s + n - i - 1]

        if cur_sum > sum:
            ans = i
            sum = cur_sum

    ans += 1
    print(ans)        


def __starting_point():
    main()

__starting_point()
