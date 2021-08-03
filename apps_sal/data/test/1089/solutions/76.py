def combination_mod(n, r, MOD=10**9 + 7):
    n_ = 1
    for i in range(1, n + 1):
        n_ = (n_ * i) % MOD
    r_ = 1
    for i in range(1, r + 1):
        r_ = (r_ * i) % MOD
    nr_ = 1
    for i in range(1, n - r + 1):
        nr_ = (nr_ * i) % MOD

    power_r = pow(r_, MOD - 2, MOD)
    power_nr = pow(nr_, MOD - 2, MOD)

    return (n_ * power_r * power_nr) % MOD


def main():
    N, M, K = list(map(int, input().split()))

    MOD = 10**9 + 7
    num = combination_mod(N * M - 2, K - 2)

    col_ans = 0
    row_ans = 0

    for i in range(1, M):
        col_ans += pow(N, 2) * (M - i) * num * i

    for i in range(1, N):
        row_ans += pow(M, 2) * (N - i) * num * i

    ans = (col_ans + row_ans) % MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
