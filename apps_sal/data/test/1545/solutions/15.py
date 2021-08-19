import sys
mod = 10 ** 9 + 7
inf = 1 << 30


def solve():
    n = int(input())
    msg = input()
    clim = [int(i) for i in input().split()]
    dp = [0] * (n + 1)
    dp[0] = 1
    max_len = 0
    for i in range(1, n + 1):
        limlen = inf
        cur_len = 0
        for j in range(i, 0, -1):
            alpha = ord(msg[j - 1]) - ord('a')
            limlen = min(limlen, clim[alpha])
            cur_len += 1
            if cur_len > limlen:
                break
            max_len = max(max_len, cur_len)
            dp[i] = (dp[i] + dp[j - 1]) % mod
    min_sp = 0
    cur_len = 0
    limlen = inf
    for ch in msg:
        cur_len += 1
        alpha = ord(ch) - ord('a')
        limlen = min(limlen, clim[alpha])
        if cur_len > limlen:
            cur_len = 1
            min_sp += 1
            limlen = clim[alpha]
    print(dp[n])
    print(max_len)
    print(min_sp + 1)


def __starting_point():
    solve()


__starting_point()
