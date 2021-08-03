# https://atcoder.jp/contests/abc159/submissions/11139734

def main():
    MOD = 998244353

    N, S = list(map(int, input().split()))
    *A, = list(map(int, input().split()))

    ans = 0
    dp = [0] * (S + 1)
    for i, a in enumerate(A, start=1):
        dp[0] = i  # i以前の(i+1)通りの起点がある（以後未取得）
        ans += dp[S]  # aを取らずにclose
        if S >= a:
            ans += dp[S - a]  # aを取ってclose
        ans %= MOD
        for s in reversed(list(range(a, S + 1))):
            dp[s] += dp[s - a]
            dp[s] %= MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
