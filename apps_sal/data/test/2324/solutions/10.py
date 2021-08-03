def main():
    s = input()
    n = len(s)
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    count = [0 for i in range(n + 1)]

    for sub_len in range(1, n + 1):
        for left in range(0, n - sub_len + 1):
            right = left + sub_len - 1

            if sub_len == 1:
                dp[left][right] = 1
            elif sub_len == 2:
                if s[left] == s[right]:
                    dp[left][right] = 2
            else:
                if s[left] == s[right] and dp[left + 1][right - 1] > 0:
                    dp[left][right] = dp[left][left + sub_len // 2 - 1] + 1

            count[dp[left][right]] += 1

    for i in range(n - 1, 0, -1):
        count[i] += count[i + 1]

    for i in range(1, n + 1):
        print(count[i], end=' ')

    print()


def __starting_point():
    main()


__starting_point()
