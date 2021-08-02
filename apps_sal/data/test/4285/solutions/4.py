MOD = 10**9 + 7


def main():
    N = int(input())
    S = input()

    pre_hatena = S[:1].count("?")
    a = S[:1].count("a")
    post_hatena = S[2:].count("?")
    c = S[2:].count("c")

    rev_3 = pow(3, MOD - 2, MOD)
    ans = 0
    for i in range(1, N - 1):
        if S[i] == "?" or S[i] == "b":
            pre_pow = pow(3, pre_hatena, MOD)
            pre = pre_pow * a + ((pre_pow * rev_3) % MOD) * pre_hatena
            post_pow = pow(3, post_hatena, MOD)
            post = post_pow * c + ((post_pow * rev_3) % MOD) * post_hatena
            ans += pre * post
            ans %= MOD
        if S[i] == "?":
            pre_hatena += 1
        if S[i] == "a":
            a += 1
        if S[i + 1] == "?":
            post_hatena -= 1
        if S[i + 1] == "c":
            c -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
