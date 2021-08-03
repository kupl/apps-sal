def main():
    def modpow(x, n, mod):
        res = 1
        while n:
            if n % 2:
                res *= x % mod
            x *= x % mod
            n >>= 1
        return res

    s = input()
    s = s[::-1]
    s_len = len(s)
    mod = 2019
    d = [0] * mod
    d[0] = 1
    rev_num = 0
    # 2以上なら共通するmodがあったということになる
    for i in range(s_len):
        rev_num += int(s[i]) * int(modpow(10, i, mod))
        rev_num %= mod
        d[rev_num] += 1
    # 2以上同じmodがあったらそこから2つ選ぶ選び方
    # それを全てのmodで
    print(sum(i * (i - 1) // 2 for i in d))


def __starting_point():
    main()


__starting_point()
