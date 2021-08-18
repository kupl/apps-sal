
def iim(): return list(map(int, input().rstrip().split()))


def resolve():
    N, S = iim()
    A = list(iim())
    mod = 998244353
    S1 = S + 1

    dp = [0] * (S + 1)

    dp[0] = pow(2, N, mod)
    inv = pow(2, mod - 2, mod)

    for ai in A:
        for i in range(S, ai - 1, -1):
            dp[i] = (dp[i] + dp[i - ai] * inv) % mod

    print((dp[-1]))


def __starting_point():
    resolve()


__starting_point()
