MOD = 10 ** 9 + 7


def main():
    S = input()
    N = len(S)
    pre_hatena = S[:1].count('?')
    a = S[:1].count('A')
    post_hatena = S[2:].count('?')
    c = S[2:].count('C')
    ans = 0
    for i in range(1, N - 1):
        if S[i] == '?' or S[i] == 'B':
            pre_pow = pow(3, pre_hatena - 1, MOD)
            pre = pre_pow * 3 % MOD * a + pre_pow * pre_hatena
            post_pow = pow(3, post_hatena - 1, MOD)
            post = post_pow * 3 % MOD * c + post_pow * post_hatena
            ans += pre * post
            ans %= MOD
        if S[i] == '?':
            pre_hatena += 1
        if S[i] == 'A':
            a += 1
        if S[i + 1] == '?':
            post_hatena -= 1
        if S[i + 1] == 'C':
            c -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
