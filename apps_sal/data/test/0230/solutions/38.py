import numpy as np


def main():
    n = int(input())
    s = list(input())
    for i in range(n):
        s[i] = ord(s[i]) - ord("a")
    s = np.array(s)
    dp = np.zeros((n + 1, n + 1), dtype=np.int64)
    tmp = np.arange(0, n + 1)
    t = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        t[i] += tmp
        tmp -= 1
    for i in range(n):
        c = s[i]
        equal = (c == s)
        dp[i + 1][1:] += equal
        dp[i + 1][1:] += equal * dp[i][:-1]
    dp = np.minimum(dp, t)
    ans = 0
    for i in range(1, n):
        tmp = dp[i][i + 1:]
        tmp = tmp[ans < tmp]
        if 0 < len(tmp):
            ans = max(ans, max(tmp))
    print((int(ans)))


def __starting_point():
    main()


__starting_point()
