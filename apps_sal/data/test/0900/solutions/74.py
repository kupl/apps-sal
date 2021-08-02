def main():
    S = [int(i) if i != '?' else -1 for i in input()]
    s = len(S)
    mod = 10 ** 9 + 7
    dp = [[0] * 13 for _ in range(s)]

    table = [[0] * 10 for _ in range(13)]
    for i in range(13):
        for j in range(10):
            table[i][j] = (i * 10 + j) % 13

    table2 = [[] for _ in range(13)]
    for i in range(13):
        for j in range(10):
            table2[table[i][j]].append(i)
    t = set(range(13))
    table2 = [t - set(i) for i in table2]

    if S[0] == -1:
        for i in range(10):
            dp[0][i] += 1
    else:
        dp[0][S[0] % 13] += 1

    for i in range(1, s):
        if S[i] == -1:
            temp = sum(dp[i - 1])
            for j in range(13):
                dp[i][j] = temp
                for k in table2[j]:
                    dp[i][j] -= dp[i - 1][k]
                dp[i][j] %= mod
        else:
            for j in range(13):
                dp[i][table[j][S[i]]] = dp[i - 1][j]

    print(dp[-1][5] % mod)


def __starting_point():
    main()


__starting_point()
