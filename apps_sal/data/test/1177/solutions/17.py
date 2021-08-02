def solve():
    MOD = 998244353

    N, S = list(map(int, input().split()))
    As = list(map(int, input().split()))

    dp1 = [0] * (S + 1)
    dp2S = 0
    for A in As:
        dp2S += dp1[S]
        if S - A >= 0:
            dp2S += dp1[S - A]
        if S - A == 0:
            dp2S += 1
        dp2S %= MOD
        for sm in reversed(list(range(A + 1, S + 1))):
            dp1[sm] += dp1[sm - A]
            dp1[sm] %= MOD
        if S - A >= 0:
            dp1[A] += dp1[0] + 1
            dp1[A] %= MOD
        dp1[0] += 1

    print(dp2S)


solve()
