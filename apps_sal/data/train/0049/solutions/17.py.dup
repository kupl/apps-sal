import sys

MAX_N = 20
MAX_DIG = 3
dp = [[0] * (MAX_DIG + 1) for i in range(MAX_N)]


def calc_dp():
    dp[0][0] = 1
    for i in range(1, MAX_N):
        dp[i][0] = 1
        for j in range(MAX_DIG):
            dp[i][j + 1] += 9 * dp[i - 1][j]
            dp[i][j + 1] += dp[i - 1][j + 1]


def first_dig(n):
    cnt = 0
    while n >= 10:
        n //= 10
        cnt += 1
    return n, cnt


def calc_ans(n):
    ans = 0
    for n_digs in range(MAX_DIG, -1, -1):
        x, cnt = first_dig(n)
        for i in range(n_digs):
            ans += x * dp[cnt][i]
        ans += dp[cnt][n_digs]
        n -= x * 10 ** cnt
    return ans


def main():
    calc_dp()
    T = int(input())
    for _ in range(T):
        l, r = map(int, input().split())
        print(calc_ans(r) - calc_ans(l - 1) if l > 0 else 0)


def __starting_point():
    main()


__starting_point()
