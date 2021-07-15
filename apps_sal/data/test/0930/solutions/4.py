MOD = 10 ** 9 + 7


def prepare(n, MOD):
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


def comb(n, r, factorials, invs):
    return factorials[n] * invs[r] * invs[n - r] % MOD


def main():
    n, k = list(map(int, input().split()))
    factorials, invs = prepare(n, MOD)
    ans = 0
    for m in range(min(k, n - 1) + 1):
        ans += comb(n - 1, m, factorials, invs) * comb(n, m, factorials, invs)
        ans %= MOD
    print(ans)


def __starting_point():
    main()

__starting_point()
