from itertools import accumulate


def solve():
    MOD = 10**9 + 7

    Ss = input()

    dp = [0] * 13
    dp[0] = 1
    for d, Sd in enumerate(Ss):
        dp2 = [0] * 26
        for mod13 in range(13):
            if Sd != '?':
                x = int(Sd)
                mod13n = (10 * mod13 + x) % 13
                dp2[mod13n] += dp[mod13]
                dp2[mod13n + 1] -= dp[mod13]
            else:
                mod13n = (10 * mod13 + 0) % 13
                dp2[mod13n] += dp[mod13]
                dp2[mod13n + 10] -= dp[mod13]
        dp2 = list(accumulate(dp2))
        dp = [(a + b) % MOD for a, b in zip(dp2[:13], dp2[13:])]

    print((dp[5]))


solve()
